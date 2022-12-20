import csv
from statistics import mean


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, "r") as data:
        data_list = data.readlines()
        formatted_student_data = [item.split(",") for item in data_list]
        for item in formatted_student_data:
            grades_str_list = item[1:]
            grades_int_list = [int(str_num) for str_num in grades_str_list]
            student_average = mean(grades_int_list)
            with open(output_file_name, mode="a") as output_file:
                output_file.write(f"{item[0]},{str(student_average)}\n")


def calculate_sorted_averages(input_file_name, output_file_name):
    sorted_list = []
    with open(input_file_name, "r") as data:
        data_list = data.readlines()
        formatted_student_data = [item.split(",") for item in data_list]
        for item in formatted_student_data:
            grades_str_list = item[1:]
            grades_int_list = [int(str_num) for str_num in grades_str_list]

            sorted_list.append([item[0], mean(grades_int_list)])
    sorted_list2 = sorted(sorted_list, key=lambda x: x[1], reverse=True)
    print(sorted_list2)
    with open(output_file_name, "a") as output_file:
        for item in sorted_list2:
            output_file.write(f"{item[0]}, {item[1]}\n")


def calculate_three_best(input_file_name):
    with open(input_file_name, "r") as data:
        data_list = data.readlines()
        formatted_student_data = [item.split(",") for item in data_list]
        for item in formatted_student_data:
            grades_str_list = item[1:]
            grades_int_list = [int(str_num) for str_num in grades_str_list]
            print(grades_int_list)

# def calculate_three_worst(input_file_name, output_file_name):


# def calculate_average_of_averages(input_file_name, output_file_name):
# calculate_averages("grades.csv", "averages.csv")
calculate_sorted_averages("grades.csv", "sorted_average.csv")
# calculate_three_best("grades.csv")
