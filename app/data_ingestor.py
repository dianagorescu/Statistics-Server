"""Module for data ingestion tasks."""
import csv

"""Reading csv format data."""
class DataIngestor:
    def __init__(self, csv_path: str):

        # Initialize the list
        self.data_list= []

        with open(csv_path, "r", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Create a dictionary for every row
            for row in reader:
                data_dict = {}
                for column, value in row.items():
                    data_dict[column] = value
                self.data_list.append(data_dict)


        self.questions_best_is_min = [
            'Percent of adults aged 18 years and older who have an overweight classification',
            'Percent of adults aged 18 years and older who have obesity',
            'Percent of adults who engage in no leisure-time physical activity',
            'Percent of adults who report consuming fruit less than one time daily',
            'Percent of adults who report consuming vegetables less than one time daily'
        ]

        self.questions_best_is_max = [
            'Percent of adults who achieve at least 150 minutes a week of '
            'moderate-intensity aerobic physical activity or 75 minutes a week of '
            'vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who achieve at least 150 minutes a week of '
            'moderate-intensity aerobic physical activity or 75 minutes a week of '
            'vigorous-intensity aerobic physical activity and engage in muscle-strengthening '
            'activities on 2 or more days a week',
            'Percent of adults who achieve at least 300 minutes a week of '
            'moderate-intensity aerobic physical activity or 150 minutes a week of '
            'vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who engage in muscle-strengthening activities on 2 or '
            'more days a week',
        ]
