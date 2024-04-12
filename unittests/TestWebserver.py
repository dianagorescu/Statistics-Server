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
        expected_result = {'Maryland': 20.0, 'California': 21.0}
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
    
    def test_global_mean(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5"},
            {"LocationDesc": "Maryland", "Question": "What is the GDP?", "Data_Value": "20.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "15.2"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.1"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "24.3"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2"},
            {"LocationDesc": "New York", "Question": "What is the state mean?", "Data_Value": "45.6"}
        ]
        done_jobs = {}
        qmin = []
        qmax = []

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question": "What is the GDP?"}

        # Call the state_mean function with the simulated data
        result = task_runner.global_mean(data_list, data_quest['question'])

        # Check if the function returns the correct result
        expected_result = {"global_mean": 25.000000000000004} 
        self.assertEqual(result, expected_result)

    def test_diff_from_mean(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5"},
            {"LocationDesc": "Maryland", "Question": "What is the GDP?", "Data_Value": "20.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Bucharest", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "15.2"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6"},
            {"LocationDesc": "Arizona", "Question": "What is the average income?", "Data_Value": "24.9"},
            {"LocationDesc": "Arizona", "Question": "What is the state mean?", "Data_Value": "30.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "21.27"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.1"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8"},
            {"LocationDesc": "New York", "Question": "What is the average income?", "Data_Value": "25.6"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "24.3"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2"},
            {"LocationDesc": "Texas", "Question": "How many individuals are currently unemployed?", "Data_Value": "75.8"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "78.2"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "77.88"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "50.2"},
            {"LocationDesc": "New York", "Question": "What is the state mean?", "Data_Value": "45.6"}
        ]
        done_jobs = {}  
        qmin = [
            'How many individuals are currently unemployed?',
            'What is the GDP?',
            'What is the average income?'
        ]
        qmax = [
            'How many individuals are below the poverty line?',
            'What is the percentage of the population that owns a home?',
            'What is the state mean?'
        ]

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question": "What is the average income?"}

        # Call the state_mean function with the simulated data
        result = task_runner.diff_from_mean(data_list, data_quest['question'])

        # Check if the function returns the correct result
        expected_result = {'Maryland': 12.311111111111114, 'Arizona': 10.211111111111116, 'New York': 9.511111111111113, 'Guam': 4.711111111111116, 'Bucharest': 4.411111111111115, 'Texas': -29.08888888888889}
        self.assertEqual(result, expected_result)


    def test_state_diff_from_mean(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5"},
            {"LocationDesc": "Maryland", "Question": "What is the GDP?", "Data_Value": "20.3"},
            {"LocationDesc": "Guam", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "30.7"},
            {"LocationDesc": "Bucharest", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Texas", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "15.2"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6"},
            {"LocationDesc": "Arizona", "Question": "What is the average income?", "Data_Value": "24.9"},
            {"LocationDesc": "Arizona", "Question": "What is the state mean?", "Data_Value": "30.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "21.27"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.1"},
            {"LocationDesc": "Arizona", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "10.5"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8"},
            {"LocationDesc": "New York", "Question": "What is the average income?", "Data_Value": "25.6"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "24.3"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2"},
            {"LocationDesc": "Texas", "Question": "How many individuals are currently unemployed?", "Data_Value": "75.8"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "78.2"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "77.88"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "50.2"},
            {"LocationDesc": "New York", "Question": "What is the state mean?", "Data_Value": "45.6"},
            {"LocationDesc": "Arizona", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "45.9"}
        ]
        done_jobs = {}  
        qmin = [
            'How many individuals are currently unemployed?',
            'What is the GDP?',
            'What is the average income?'
        ]
        qmax = [
            'How many individuals are below the poverty line?',
            'What is the percentage of the population that owns a home?',
            'What is the state mean?'
        ]

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question_data": "What is the percentage of the population that owns a home?", "nume_stat": "Arizona"}

        # Call the state_mean function with the simulated data
        result = task_runner.state_diff_from_mean(data_list, data_quest)

        # Check if the function returns the correct result
        expected_result = {'Arizona': -2.625}
        self.assertEqual(result, expected_result)


    def test_best5(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5"},
            {"LocationDesc": "Maryland", "Question": "What is the GDP?", "Data_Value": "20.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Bucharest", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "15.2"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6"},
            {"LocationDesc": "Arizona", "Question": "What is the average income?", "Data_Value": "24.9"},
            {"LocationDesc": "Arizona", "Question": "What is the state mean?", "Data_Value": "30.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "21.27"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.1"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8"},
            {"LocationDesc": "New York", "Question": "What is the average income?", "Data_Value": "25.6"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "24.3"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2"},
            {"LocationDesc": "Texas", "Question": "How many individuals are currently unemployed?", "Data_Value": "75.8"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "78.2"},
            {"LocationDesc": "Texas", "Question": "How many individuals are below the poverty line?", "Data_Value": "74.18"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "50.2"},
            {"LocationDesc": "New York", "Question": "What is the state mean?", "Data_Value": "45.6"},
            {"LocationDesc": "Bucharest", "Question": "How many individuals are below the poverty line?", "Data_Value": "75.87"},
            {"LocationDesc": "Guam", "Question": "How many individuals are below the poverty line?", "Data_Value": "71.18"},
            {"LocationDesc": "Arizona", "Question": "How many individuals are below the poverty line?", "Data_Value": "23.66"},
            {"LocationDesc": "Texas", "Question": "How many individuals are below the poverty line?", "Data_Value": "20.18"},
            {"LocationDesc": "Texas", "Question": "How many individuals are below the poverty line?", "Data_Value": "72.668"}

        ]
        done_jobs = {}  
        qmin = [
            'How many individuals are currently unemployed?',
            'What is the GDP?',
            'What is the average income?'
        ]
        qmax = [
            'How many individuals are below the poverty line?',
            'What is the percentage of the population that owns a home?',
            'What is the state mean?'
        ]

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question": "What is the average income?"}

        # Call the state_mean function with the simulated data
        result = task_runner.best5(data_list, data_quest['question'])

        # Check if the function returns the correct result
        expected_result = {'Maryland': 22.8, 'Arizona': 24.9, 'New York': 25.6, 'Guam': 30.4, 'Bucharest': 30.7}
        self.assertEqual(result, expected_result)

    def test_worst5(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5"},
            {"LocationDesc": "Maryland", "Question": "What percentage of households have pets?", "Data_Value": "99.3"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Bucharest", "Question": "What is the average income?", "Data_Value": "30.7"},
            {"LocationDesc": "Texas", "Question": "What percentage of households have pets?", "Data_Value": "15.2"},
            {"LocationDesc": "New York", "Question": "What percentage of households have pets?", "Data_Value": "25.6"},
            {"LocationDesc": "Arizona", "Question": "What is the average income?", "Data_Value": "24.9"},
            {"LocationDesc": "Dublin", "Question": "What percentage of households have pets?", "Data_Value": "10.9"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "21.27"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9"},
            {"LocationDesc": "Arizona", "Question": "What percentage of households have pets?", "Data_Value": "11.9"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3"},
            {"LocationDesc": "Guam", "Question": "What percentage of households have pets?", "Data_Value": "30.1"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8"},
            {"LocationDesc": "New York", "Question": "What percentage of households have pets?", "Data_Value": "25.6"},
            {"LocationDesc": "Maryland", "Question": "What percentage of households have pets?", "Data_Value": "24.3"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2"},
            {"LocationDesc": "Texas", "Question": "How many individuals are currently unemployed?", "Data_Value": "75.8"},
            {"LocationDesc": "Texas", "Question": "What percentage of households have pets?", "Data_Value": "78.2"},
            {"LocationDesc": "Texas", "Question": "How many individuals are below the poverty line?", "Data_Value": "74.18"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "50.2"},
            {"LocationDesc": "New York", "Question": "What percentage of households have pets?", "Data_Value": "2.6"},
            {"LocationDesc": "Bucharest", "Question": "What percentage of households have pets?", "Data_Value": "75.87"},
            {"LocationDesc": "Guam", "Question": "How many individuals are below the poverty line?", "Data_Value": "71.18"},
            {"LocationDesc": "Arizona", "Question": "How many individuals are below the poverty line?", "Data_Value": "23.66"},
            {"LocationDesc": "Texas", "Question": "How many individuals are below the poverty line?", "Data_Value": "20.18"},
            {"LocationDesc": "Texas", "Question": "How many households have children under the age of 18?", "Data_Value": "0.03"}

        ]
        done_jobs = {}  
        qmin = [
            'How many individuals are currently unemployed?',
            'What is the GDP?',
            'What percentage of households have pets?'
        ]
        qmax = [
            'How many individuals are below the poverty line?',
            'What is the percentage of the population that owns a home?',
            'What is the average income?'
        ]

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question": "What percentage of households have pets?"}

        # Call the state_mean function with the simulated data
        result = task_runner.worst5(data_list, data_quest['question'])

        # Check if the function returns the correct result
        expected_result = {'Bucharest': 75.87, 'Maryland': 61.8, 'Texas': 46.7, 'Guam': 30.1, 'New York': 17.933333333333334}
        self.assertEqual(result, expected_result)

    def test_state_mean_by_category(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "20.3", "StratificationCategory1": "Gender", "Stratification1":"Male"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "30.7", "StratificationCategory1": "Age (years)", "Stratification1":"35 - 44"},
            {"LocationDesc": "Bucharest", "Question": "What is the average income?", "Data_Value": "30.7", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.2", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Arizona", "Question": "What is the average income?", "Data_Value": "24.9", "StratificationCategory1": "Age (years)", "Stratification1":""},
            {"LocationDesc": "Arizona", "Question": "What is the state mean?", "Data_Value": "30.9", "StratificationCategory1": "Gender", "Stratification1":"Male"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "21.27", "StratificationCategory1": "Gender", "Stratification1":"Male"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "25.9", "StratificationCategory1": "Age (years)", "Stratification1":"35 - 44"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.1", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Arizona", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "10.5", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "New York", "Question": "What is the average income?", "Data_Value": "25.6", "StratificationCategory1": "Age (years)", "Stratification1":"35 - 44"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "24.3", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7", "StratificationCategory1": "Education", "Stratification1":"Highschool"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2", "StratificationCategory1": "Education", "Stratification1":"Highschool"},
            {"LocationDesc": "Texas", "Question": "How many individuals are currently unemployed?", "Data_Value": "75.8", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "78.2", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "77.88", "StratificationCategory1": "Education", "Stratification1":"Highschool"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "50.2", "StratificationCategory1": "Education", "Stratification1":"College"},
            {"LocationDesc": "New York", "Question": "What is the state mean?", "Data_Value": "45.6", "StratificationCategory1": "Education", "Stratification1":"College"},
            {"LocationDesc": "Arizona", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "45.9", "StratificationCategory1": "Education", "Stratification1":"College"}
        ]
        done_jobs = {}  
        qmin = [
            'How many individuals are currently unemployed?',
            'What is the GDP?',
            'What is the average income?'
        ]
        qmax = [
            'How many individuals are below the poverty line?',
            'What is the percentage of the population that owns a home?',
            'What is the state mean?'
        ]

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question_data": "What is the GDP?", "nume_stat": "Texas"}

        # Call the state_mean function with the simulated data
        result = task_runner.state_mean_by_category(data_list, data_quest)

        # Check if the function returns the correct result
        expected_result = {'Texas': {"('Age (years)', '25 - 34')": 15.5, "('Age (years)', '35 - 44')": 25.9, "('Gender', 'Male')": 20.785}}
        self.assertEqual(result, expected_result)


    def test_mean_by_category(self):
        coada_joburi = []
        data_list = [
            {"LocationDesc": "Guam", "Question": "What is the average temperature?", "Data_Value": "10.5", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "20.3", "StratificationCategory1": "Gender", "Stratification1":"Male"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "30.7", "StratificationCategory1": "Age (years)", "Stratification1":"35 - 44"},
            {"LocationDesc": "Bucharest", "Question": "What is the average income?", "Data_Value": "30.7", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.2", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "New York", "Question": "What is the GDP?", "Data_Value": "25.6", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Arizona", "Question": "What is the average income?", "Data_Value": "24.9", "StratificationCategory1": "Age (years)", "Stratification1":""},
            {"LocationDesc": "Arizona", "Question": "What is the state mean?", "Data_Value": "30.9", "StratificationCategory1": "Gender", "Stratification1":"Male"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "21.27", "StratificationCategory1": "Gender", "Stratification1":"Male"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "25.9", "StratificationCategory1": "Age (years)", "Stratification1":"35 - 44"},
            {"LocationDesc": "Arizona", "Question": "What is the education level?", "Data_Value": "22.9", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "21.3", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Guam", "Question": "What is the average income?", "Data_Value": "30.1", "StratificationCategory1": "Gender", "Stratification1":"Female"},
            {"LocationDesc": "Arizona", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "10.5", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Arizona", "Question": "What is the average temperature?", "Data_Value": "25.9", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the GDP?", "Data_Value": "15.8", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "New York", "Question": "What is the average income?", "Data_Value": "25.6", "StratificationCategory1": "Age (years)", "Stratification1":"35 - 44"},
            {"LocationDesc": "Maryland", "Question": "What is the average income?", "Data_Value": "24.3", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Guam", "Question": "What is the GDP?", "Data_Value": "37.7", "StratificationCategory1": "Education", "Stratification1":"Highschool"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "75.2", "StratificationCategory1": "Education", "Stratification1":"Highschool"},
            {"LocationDesc": "Texas", "Question": "How many individuals are currently unemployed?", "Data_Value": "75.8", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "78.2", "StratificationCategory1": "Age (years)", "Stratification1":"25 - 34"},
            {"LocationDesc": "Texas", "Question": "What is the state mean?", "Data_Value": "77.88", "StratificationCategory1": "Education", "Stratification1":"Highschool"},
            {"LocationDesc": "Texas", "Question": "What is the average income?", "Data_Value": "50.2", "StratificationCategory1": "Education", "Stratification1":"College"},
            {"LocationDesc": "New York", "Question": "What is the state mean?", "Data_Value": "45.6", "StratificationCategory1": "Education", "Stratification1":"College"},
            {"LocationDesc": "Arizona", "Question": "What is the percentage of the population that owns a home?", "Data_Value": "45.9", "StratificationCategory1": "Education", "Stratification1":"College"}
        ]
        done_jobs = {}  
        qmin = [
            'How many individuals are currently unemployed?',
            'What is the GDP?',
            'What is the average income?'
        ]
        qmax = [
            'How many individuals are below the poverty line?',
            'What is the percentage of the population that owns a home?',
            'What is the state mean?'
        ]

        # Initialize an instance of the TaskRunner class
        task_runner = TaskRunner(coada_joburi, data_list, done_jobs, qmin, qmax)

        # Define input data for the function
        data_quest = {"question": "What is the GDP?"}

        # Call the state_mean function with the simulated data
        result = task_runner.mean_by_category(data_list, data_quest['question'])

        # Check if the function returns the correct result
        expected_result = {"('Guam', 'Age (years)', '35 - 44')": 30.7, "('Guam', 'Education', 'Highschool')": 37.7, "('New York', 'Age (years)', '25 - 34')": 25.6, "('Texas', 'Age (years)', '25 - 34')": 15.5, "('Texas', 'Age (years)', '35 - 44')": 25.9, "('Texas', 'Gender', 'Male')": 20.785} 
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
    