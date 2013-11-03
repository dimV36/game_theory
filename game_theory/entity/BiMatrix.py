__author__ = 'dimv36'
from numpy import *


class BiMatrix:
    def __init__(self, first, second):
        self.first = array(first)
        self.second = array(second)

    def __eq__(self, other):
        if self.size() == other.size():
            if all(abs(self.first - other.first) < pow(10, -6)) and all(abs(self.second - other.second) < pow(10, -6)):
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if self.size() == other.size():
            if all(self.first > other.first) and all(self.second > other.second):
                return True
        return False

    def __lt__(self, other):
        if self.size() == other.size():
            if all(self.first < other.first) and all(self.second < other.second):
                return True
        return False

    def __iter__(self):
        return

    def __mul__(self, other):
        return BiMatrix(self.first * other.first, self.second * other.second)

    def __contains__(self, item):
        return item.first.__contains__(self.first) and item.second.__contains__(self.second)

    def __str__(self):
        length = self.first.shape
        string = 'BiMatrix:\n'
        for i in range(0, length[0]):
            for j in range(0, length[1]):
                string += str(self.first[i, j]) + ';' + str(self.second[i, j]) + '\t'
            string += "\n"
        return string

    def __repr__(self):
        length = self.first.shape
        string = ''
        for i in range(0, length[0]):
            for j in range(0, length[1]):
                string += str(self.first[i, j]) + ';' + str(self.second[i, j])
        return string

    def copy(self):
        """
        @return: Возвращает полную копию объекта self
        """
        name = self.__class__
        result = name.__new__(name)
        result.first = copy(self.first)
        result.second = copy(self.second)
        return result

    def find(self, bi_element):
        """
        Получить индекс(ы) элемента, заданным параметром bi_element
        @param bi_element: элемент BiMatrix, заданный объектом BiMatrix
        @return: Возвращает список списков индексов матрицы, в случае, если элемент bi_element найден.
        Иначе возвращается [[-1, -1]]
        """
        result = []
        for i in range(0, self.row_count()):
            for j in range(0, self.column_count()):
                if self.first[i, j] == bi_element.first and self.second[i, j] == bi_element.second:
                    result.extend([i, j])
        if len(result) == 0:
            return list([-1, -1])
        else:
            return result

    def item(self, first_index, second_index):
        """
        Получить элемент BiMatrix, заданный индексами first_index, second_index
        @param first_index: индекс строки
        @param second_index: индекс столбца
        @return: Элемент матрицы
        """
        first_element = array([[self.first[first_index, second_index]]])
        second_element = array([[self.second[first_index, second_index]]])
        return BiMatrix(first_element, second_element)

    def row_neighboring(self, first_index, second_index):
        """
        Получить соседние элементы в строке элемента, заданному индексами
        @param first_index: Индекс строки
        @param second_index: Индекс столбца
        @return: Список сущностей BiMatrix - соседи элемента, заданного индексами
        """
        result = []
        if first_index - 1 >= 0:
            result.append(self.item(first_index - 1, second_index))
        if first_index + 1 < self.row_count():
            result.append(self.item(first_index + 1, second_index))
        return result

    def column_neighboring(self, first_index, second_index):
        """
        Получить соседние элементы в столбце элемента, заданного индексами
        @param first_index: Индекс строки
        @param second_index: Индекс столбца
        @return: Список сущностей BiMatrix - соседи элемента, заданного индексами
        """
        result = []
        if second_index - 1 >= 0:
            result.append(self.item(first_index, second_index - 1))
        if second_index + 1 < self.column_count():
            result.append(self.item(first_index, second_index + 1))
        return result

    def all_elements_without_current(self, first_index, second_index):
        """
        Получить все элементы матрицы кроме текущего элемента, заданного индексами
        @param first_index: Индекс строки
        @param second_index: Индекс столбца
        @return: Список элементов, содержащий элементы матрицы без текущего элемента
        """
        result = []
        for i in range(0, self.row_count()):
            for j in range(0, self.column_count()):
                if not(i == first_index and j == second_index):
                    result.append(self.item(i, j))
        return result

    def row_count(self):
        """
        Получить число строк biMatrix
        @return: Число строк biMatrix
        """
        return self.size()[0]

    def column_count(self):
        """
        Получить число столбцов biMatrix
        @return: Число столбцов biMatrix
        """
        return self.size()[1]

    def size(self):
        """
        Получить размер BiMatrix
        @return: Кортеж размерностей
        """
        return self.first.shape
