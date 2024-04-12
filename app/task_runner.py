from queue import Queue
from threading import Thread
from collections import defaultdict

import itertools
import json
import os
import multiprocessing

class ThreadPool:
    def __init__(self, data_ingestor):

        self.data_list = data_ingestor.data_list

        # Transfer lists with questions for tasks best5/ worst5
        self.qmin = data_ingestor.questions_best_is_min
        self.qmax = data_ingestor.questions_best_is_max

        # Set the number of threads
        n_threads = os.getenv('TP_NUM_OF_THREADS')
        if n_threads:
            self.n_threads = n_threads
        else:
            self.n_threads = multiprocessing.cpu_count()

        self.coada_joburi = Queue()
        self.threads = []
        self.done_jobs = []

        for _ in range (self.n_threads):
            thread = TaskRunner(self.coada_joburi,
                                self.data_list,
                                self.done_jobs,
                                self.qmin,
                                self.qmax)
            thread.start()
            self.threads.append(thread)

    def graceful_shutdown(self):
        for _ in range(self.n_threads):
            self.coada_joburi.put(None)

        for thread in self.threads:
            thread.join()


class TaskRunner(Thread):
    def __init__(self, coada_joburi,data_list, done_jobs, qmin, qmax):

        # Initialize necessary structures
        Thread.__init__(self)
        self.coada_joburi = coada_joburi
        self.data_list = data_list
        self.done_jobs = done_jobs

        self.qmin = qmin
        self.qmax = qmax

    def run(self):
        while True:

            result = {}
            job = self.coada_joburi.get()

            if job['nume_job'] == "states_mean":
               result = self.states_mean(self.data_list, job['question_data'])
            elif job['nume_job'] == "state_mean":
                result = self.state_mean(self.data_list, job)
            elif job['nume_job'] == "best5":
                result = self.best5(self.data_list, job['question_data'])
            elif job['nume_job'] == "worst5":
                result = self.worst5(self.data_list, job['question_data'])
            elif job['nume_job'] == "global_mean":
                result = self.global_mean(self.data_list, job['question_data'])
            elif job['nume_job'] == "diff_from_mean":
                result = self.diff_from_mean(self.data_list, job['question_data'])
            elif job['nume_job'] == "state_diff_from_mean":
                result = self.state_diff_from_mean(self.data_list, job)
            elif job['nume_job'] == "state_mean_by_category":
                result = self.state_mean_by_category(self.data_list, job)
            elif job['nume_job'] == "mean_by_category":
                result = self.mean_by_category(self.data_list, job['question_data'])

            # Create the 'results' folder.
            # Write to the corresponding job file in JSON format.

            os.makedirs("results", exist_ok=True)
            file_path = f"results/job_{job['job_id']}.json"
            with open(file_path, "w", encoding='utf-8') as f:
                json.dump(result, f)

            # Ensure that the job activity has finished
            # and add its ID to the list of completed jobs

            job['status'] = "done"
            self.done_jobs.append(job['job_id'])

    def states_mean(self, data_list, quest):

        # Defined with defaultdict to simplify the addition and
        # accessing of data
        result = defaultdict(lambda: 0)
        contor = defaultdict(lambda: 0)

        for di in data_list:
            quest_name = di.get("Question")

            # Update the dictionaries only if the question matches
            if quest == quest_name:
                state_name = di.get("LocationDesc")
                result[state_name] += float(di.get("Data_Value"))
                contor[state_name] += 1

        for state_name, suma in result.items():
            result[state_name] = suma / contor[state_name]

        # Sort by means
        return dict(sorted(result.items(), key=lambda item: item[1] ))


    def state_mean(self, data_list, data_quest):
        suma = 0
        contor = 0
        quest_state_name = data_quest['nume_stat']
        quest_name = data_quest['question_data']

        for di in data_list:

            state_name = di.get("LocationDesc")
            quest = di.get("Question")

            # Update the variables only if the data matches
            if state_name == quest_state_name and quest == quest_name:
                suma += float(di.get("Data_Value"))
                contor += 1

        medie = suma / contor

        result = {quest_state_name : medie}
        return result


    def best5(self, data_list, quest):

        sorted_di = self.states_mean( data_list, quest)

        # Determine the type of best of the question
        if quest in self.qmin:
            # For best = min, I return the first 5
            return dict(itertools.islice(sorted_di.items(), 5))

        # For best = max, I return the last 5
        return dict(itertools.islice(reversed(sorted_di.items()), 5))

    def worst5(self, data_list, quest):

        sorted_di = self.states_mean( data_list, quest)

        # Decid tipul intrebarii best
        if quest in self.qmax:
            # For best = max, I return the first 5
            return dict(itertools.islice(sorted_di.items(), 5))

        # For best = min, I return the last 5
        return dict(itertools.islice(reversed(sorted_di.items()), 5))


    def global_mean(self, data_list, quest):
        suma = 0
        contor = 0

        for di in data_list:
            quest_name = di.get("Question")
            if quest == quest_name:
                suma += float(di.get("Data_Value"))
                contor += 1

        medie = suma / contor

        # Construct the corresponding format
        result = {"global_mean" : medie}
        return result


    def diff_from_mean(self, data_list, quest):

        # Initialize necessary variables
        medie_globala = self.global_mean(data_list, quest)['global_mean']
        d1 = self.states_mean(data_list, quest)

        # Iterate and subtract the average_stat from the global one
        for state_name, suma in d1.items():
            d1[state_name] = medie_globala - suma

        return d1

    def state_diff_from_mean(self, data_list, data_quest):

        # Initialize necessary variables
        quest_name = data_quest['question_data']
        state_name = data_quest['nume_stat']

        medie_stat = self.state_mean(data_list, data_quest)[state_name]
        medie_globala = self.global_mean(data_list, quest_name)['global_mean']

        # Calculate a simple difference
        result = {state_name : medie_globala - medie_stat}
        return result

    def state_mean_by_category(self, data_list, data_quest):

        # Initialize necessary variables
        quest_state_name = data_quest['nume_stat']
        quest_name = data_quest['question_data']

        # Defined with defaultdict to simplify the addition and
        # accessing of data
        mean = defaultdict(lambda: 0)
        contor = defaultdict(lambda: 0)

        for di in data_list:
            state_name = di.get("LocationDesc")
            quest = di.get("Question")

            # If the state name and the question match, made a tuple
            # formed by the StratificationCategory1 and its segment
            # which will be the key for the mean dictionary
            if state_name == quest_state_name and quest == quest_name:
                tu = (di.get("StratificationCategory1"), di.get("Stratification1"))
                mean[str(tu)] += float(di.get("Data_Value"))
                contor[str(tu)] += 1

        for k, m in mean.items():
            mean[k] = m / contor[k]

        # Sorted by (StratificationCategory1, Stratification1)
        res = dict(sorted(mean.items()))

        # Construct the corresponding format
        result = {quest_state_name: res}
        return result

    def mean_by_category(self, data_list, quest):

        # Defined with defaultdict to simplify the addition and
        # accessing of data
        mean = defaultdict(lambda: 0)
        contor = defaultdict(lambda: 0)

        for di in data_list:
            state_name = di.get("LocationDesc")
            quest_name = di.get("Question")

            # If the question matches, made a tuple
            # formed by the name of the state, StratificationCategory1
            # and its segment, which will be the key for the mean dictionary
            if quest == quest_name:
                if di.get("StratificationCategory1") != 'Nan':
                    tu = (state_name, di.get("StratificationCategory1"), di.get("Stratification1"))
                    mean[str(tu)] += float(di.get("Data_Value"))
                    contor[str(tu)] += 1

        for k, m in mean.items():
            mean[k] = m / contor[k]

        # Sorted by (State, StratificationCategory1, Stratification1)
        result = dict(sorted(mean.items()))

        return result
