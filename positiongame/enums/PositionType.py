__author__ = 'dimv36'
from utils.enum import EnumValue


class PositionType():
    not_defined = EnumValue(index=0, value="Неопределенная")
    root = EnumValue(index=1, value="Начальная")
    intermediate = EnumValue(index=2, value="Промежуточная")
    leaf = EnumValue(index=3, value="Терминальная")