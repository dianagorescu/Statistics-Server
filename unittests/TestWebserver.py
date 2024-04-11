import unittest

from task_runner import TaskRunner

class TestAPI(unittest.TestCase):

    def test_states_mean(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "California", "Question": "What is the state mean?", "Data_Value": "10"},
            {"LocationDesc": "Maryland", "Question": "What is the state mean?", "Data_Value": "20"},
            {"LocationDesc": "California", "Question": "What is the global mean?", "Data_Value": "30"},
            {"LocationDesc": "California", "Question": "What is the state mean?", "Data_Value": "32"}
        ]
        done_jobs = {}  
        qmin = []
        qmax = []

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question": "What is the state mean?"}

        # Call the state_mean function with the simulated data
        result = task_runner.states_mean(data_list, data_quest['question'])

        # Check if the function returns the correct result
        expected_result = {"California": 21.0, "Maryland": 20.0}
        self.assertEqual(result, expected_result)

    def test_state_mean(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "20.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "15.2"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9"}
        ]
        done_jobs = {}  
        qmin = []
        qmax = []

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question_data": "What is the average income?", "nume_stat": "Guam"}

        # Call the state_mean function with the simulated data
        result = task_runner.state_mean(data_list, data_quest)

        # Check if the function returns the correct result
        expected_result = {"Guam": 30.7} 
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
    