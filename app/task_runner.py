from queue import Queue
from threading import Thread, Event
from collections import defaultdict

import time
import itertools 
import json
import os
import multiprocessing

class ThreadPool:
    def __init__(self, data_ingestor):

        self.data_list = data_ingestor.data_list

        # Transfer listele cu categorii pentru taskul best5/ worst5
        self.qmin = data_ingestor.questions_best_is_min
        self.qmax = data_ingestor.questions_best_is_max


        n_threads = os.getenv('TP_NUM_OF_THREADS')
        
        if n_threads:
            self.n_threads = n_threads
        else:
            self.n_threads = multiprocessing.cpu_count()
        

        self.coada_joburi = Queue()
        self.threads = []
        self.done_jobs = []

        for i in range (self.n_threads):
            thread = TaskRunner(self.coada_joburi, self.data_list, self.done_jobs, self.qmin, self.qmax)
            thread.start()
            self.threads.append(thread)

    def graceful_shutdown(self):
        
        for _ in range(self.n_threads):
            self.coada_joburi.put(None)

        for thread in self.threads:
            thread.join()


class TaskRunner(Thread):
    def __init__(self, coada_joburi,data_list, done_jobs, qmin, qmax):

        # initiatilizez structuri necesare

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
            

            # Construiesc folderul results
            # Scriu in fisierul cu jobul corespunzator in format json

            os.makedirs("results", exist_ok=True)
            file_path = f"results/job_{job['job_id']}.json"
            with open(file_path, "w") as f:
                json.dump(result, f)

            # Asigur ca s a terminat activitatea jobului
            # si adaug id-ul acestuia in lista de joburi terminate

            job['status'] = "done"
            self.done_jobs.append(job['job_id'])

    def states_mean(self, data_list, quest):
        
        # Am definit cu defaultdict pentru a simplifica adaugarea si 
        # accesarea datelor

        result = defaultdict(lambda: 0) 
        contor = defaultdict(lambda: 0) 

        for di in data_list:
            quest_name = di.get("Question")

            # Actualizez dictionarele doar daca intrebarea corespunde
            if quest == quest_name:
                state_name = di.get("LocationDesc")
                result[state_name] += float(di.get("Data_Value"))
                contor[state_name] += 1

        for state_name, sum in result.items():
            result[state_name] = sum / contor[state_name]
        
        # Sortez crecator dupa medie
        return dict(sorted(result.items(), key=lambda item: item[1] ))
    

    def state_mean(self, data_list, data_quest):
        suma = 0
        contor = 0
        quest_state_name = data_quest['nume_stat']
        quest_name = data_quest['question_data']

        for dict in data_list:

            state_name = dict.get("LocationDesc")
            quest = dict.get("Question")

            # Actualizez variabilele doar daca datele corespund
            if state_name == quest_state_name and quest == quest_name:
                suma += float(dict.get("Data_Value"))
                contor += 1

        medie = suma / contor

        result = {quest_state_name : medie}
        return result


    def best5(self, data_list, quest):

        # Folosesc functia facuta mai sus
        sorted_di = self.states_mean( data_list, quest)
        
        # Decid tipul intrebarii best
        if quest in self.qmin:

            # Pentru best = min, returnez primele 5
            return dict(itertools.islice(sorted_di.items(), 5))
        else:

            # Pentru best = max, returnez ultimele 5
            return dict(itertools.islice(reversed(sorted_di.items()), 5))

    def worst5(self, data_list, quest):

        # Folosesc functia facuta mai sus
        sorted_di = self.states_mean( data_list, quest)

        # Decid tipul intrebarii best
        if quest in self.qmax:

            # Pentru best = max, returnez primele 5
            return dict(itertools.islice(sorted_di.items(), 5))
        else:
            # Pentru best = min, returnez ultimele 5
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

        # Construiesc rezultatul corespunzator
        result = {"global_mean" : medie}
        return result


    def diff_from_mean(self, data_list, quest):

        # Initializez variabile necesare
        medie_globala = self.global_mean(data_list, quest)['global_mean']
        d1 = self.states_mean(data_list, quest)

        # Iterez prin dictionar si scad media_stat din cea globala
        for state_name, sum in d1.items():
            d1[state_name] = medie_globala - sum

        return d1

    def state_diff_from_mean(self, data_list, data_quest):

        quest_name = data_quest['question_data']
        state_name = data_quest['nume_stat']

        medie_stat = self.state_mean(data_list, data_quest)[state_name]
        medie_globala = self.global_mean(data_list, quest_name)['global_mean']

        result = {state_name : medie_globala - medie_stat}
        return result

    def state_mean_by_category(self, data_list, data_quest):

        # quest_state_name = data_quest['nume_stat']
        # quest_name = data_quest['question_data']

        # mean = defaultdict(lambda: 0)
        # contor = defaultdict(lambda: 0)

        # for dict in data_list:
        #     state_name = dict.get("LocationDesc")
        #     quest = dict.get("Question")

        #     # Construiesc media pe acelasi principiu, schimband doar 
        #     # coloana de interes
        #     if state_name == quest_state_name and quest == quest_name:
        #         mean[(dict.get("StratificationCategory1"), dict.get("Stratification1"))] += float(dict.get("Data_Value"))
        #         contor[(dict.get("StratificationCategory1"), dict.get("Stratification1"))] += 1
                
        
        # for k, m in mean.items():
        #     mean[k] = m / contor[k]

        # lis = sorted(mean.items())
        # d = {}
        # for k, m in lis:
        #     d[k] = m
        
        # # Construiesc rezultatul corespunzator
        # result = {quest_state_name: d}
        return {}
    
    def mean_by_category(self, data_list, quest):

        result = {}
        # list_states = []
        # for dict in data_list:
        #     quest_name = dict.get("Question")
        #     state_name = dict.get("LocationDesc")

        #     # Construiesc o lista cu numele statelor de interes si o sortez
        #     if quest == quest_name and state_name not in list_states:
        #         list_states.append(state_name)
        # list_states = sorted(list_states)

        # for s in list_states:

        #     # Construiesc un input corespunzator pentru a apela 
        #     # functia pe un singur stat
        #     data_quest = {"question_data":quest,
        #               "nume_stat":s}
        #     res = self.state_mean_by_category(data_list, data_quest)[s]
            
        #     # Inserez numele statului pentru a respecta formatul outputului
        #     for i, mean_value in res.items():
        #         l = list(i)
        #         l.insert(0, s)
        #         result[tuple(l)] = mean_value    

        return result

         


        