import csv
# For the average
from statistics import mean 
import pandas

def calculate_averages(input_file_name, output_file_name):
    all_grades = pandas.read_csv(input_file_name)    
    print(all_grades)

# def calculate_sorted_averages(input_file_name, output_file_name):
    


# def calculate_three_best(input_file_name, output_file_name):
    


# def calculate_three_worst(input_file_name, output_file_name):
    


# def calculate_average_of_averages(input_file_name, output_file_name):
calculate_averages("grades.csv")