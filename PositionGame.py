__author__ = 'dimv36'
from platform import system
from subprocess import check_call
from positiongame import *


class PositionGame():

    @staticmethod
    def set_root(name_information_set, node):
        pass

    @staticmethod
    def add_action(action):
        pass

    @staticmethod
    def change_node_by_leaf(node_old, leaf):
        pass

    @staticmethod
    def add_leaf(previous_node, leaf):
        pass

    @staticmethod
    def to_dot():
        pass

    @staticmethod
    def to_bimatrix():
        pass

    @staticmethod
    def do_dot(file_name="", script_file=""):
        if script_file == "":
            png_name = file_name.split(".")[0]
            if system() == "Linux":
                command = "/usr/bin/dot " + file_name + " -o " + png_name + ".png -Tpng"
                if check_call(command, shell=True) == 0:
                    print("Успешно сконвертировано в {0}.png".format(png_name))
                else:
                    print("Ошибка при конвертации")
            if system() == "Windows":
                command = "\"C:\Program Files (x86)\Graphviz2.34\\bin\dot.exe\" " + "\"{0}\"".format(file_name) + " -o " + "{0}".format(png_name) + ".png -Tpng"
                print(command)
                if check_call(command, shell=True) == 0:
                    print("Успешно сконвертировано в {0}.png".format(png_name))
                else:
                    print("Ошибка при конвертации")
        else:
            script = open(script_file, 'r')
            command = script.read()
            print(command)
            if check_call(command, shell=True) == 0:
                print("Конвертация прошла успешно")
            else:
                print("Ошибка при конвертации")


if __name__ == "__main__":
    PositionGame.do_dot(script_file="C:\examples\dot.cmd")