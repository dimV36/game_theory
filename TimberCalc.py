__author__ = 'dimv36'
from numpy import *


def append(timber_list, count, timber):
    for i in range(0, count):
        timber_list.append(timber)
    return timber_list


def calc_timber(tasks, input_data):
    """
    @param tasks:
    @param input_data:
    @return:
    """
    if input_data.sum() < input_data.sum():
        print("Невозможное задание")
        return 0
    else:
        tasks_copy = tasks.copy()
#        print(input_data)
        fraction = array([])
        while True:
            max_task = max(tasks_copy)
            if max_task == 0:
                break
            task_arg = argmax(tasks_copy)
            tasks_copy[task_arg] = tasks_copy[task_arg] - max_task
#            for element in input_data:
#             for i in range(0, input_data.size):
#                if element - max_task > 0:
#                    input_data = element - max_task
        print(tasks_copy)
        print(input_data)

if __name__ == "__main__":
    tasks_list = []
    append(tasks_list, 3, 1.0)
    append(tasks_list, 2, 1.5)
    input_list = []
    append(input_list, 10, 2.7)
    append(input_list, 20, 3.5)
    tasks = array(tasks_list)
    input_data = array(input_list)
#    print(tasks)
#    print(input_data)
    calc_timber(tasks, input_data)