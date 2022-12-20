import csv
from statistics import mean


def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name, "r") as data:

        data_list = data.readlines()

        formatted_student_data = [item.split(",") for item in data_list]
        for item in formatted_student_data:
            grades_str_list = item[1:]
            grades_int_list = [int(str_num) for str_num in grades_str_list]
            print(item[0], end=" ")
            print(mean(grades_int_list))
            with open("aver")
            # print(item[0], mean(grades_int_list))
        # global grade_int_list
        # grades_list = all_grades.readlines()
        # sorted_grade_list = []
        # name_list = []
        # for person in grades_list:
        #     start = person.find(",")
        #     student_name = person[0: start]
        #     name_list.append(student_name)

        #     grade_str_list = (person[start + 1: -1].split(","))
        #     grade_int_list = [int(string_grade)
        #                       for string_grade in grade_str_list]
        #     sorted_grade_list.append(grade_int_list)
        #     print(grade_int_list)
        #     grade_mean = mean(grade_int_list)
        #     print(grade_mean)

        # print(sorted_grade_list)
        # print(name_list)
        # sorted_list_average = [mean(item) for item in sorted_grade_list]
        # print(sorted(sorted_list_average))

        # for name in name_list:
        #     print(f"{name},")
        # with open(output_file_name, "w") as average:
        #     average.write(f"{student_name}:{grade_mean}\n")


def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name, "r") as all_grades:
        global grade_int_list
        grades_list = all_grades.readlines()
        sorted_list = []
        for person in grades_list:
            start = person.find(",")
            student_name = person[0: start]
            grade_str_list = (person[start + 1: -1].split(","))
            grade_int_list = sorted([int(string_grade)
                                    for string_grade in grade_str_list])
            sorted_list.append(grade_int_list)
            print(grade_int_list)
            grade_mean = mean(grade_int_list)
        print(sorted_list)
        # with open(output_file_name, "w") as average:
        #     average.write(f"{student_name}:{grade_mean}\n")

# def calculate_three_best(input_file_name, output_file_name):


# def calculate_three_worst(input_file_name, output_file_name):

# def calculate_average_of_averages(input_file_name, output_file_name):
calculate_averages("grades.csv", "average.csv")
# calculate_sorted_averages("grades.csv", "sorted_average.csv")
