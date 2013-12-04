__author__ = 'dimv36'
import logging

logger = logging.getLogger(__name__)


class EnumConstructionException(Exception):
    """
    Raised whenever there's an error in an Enum's declaration.
    """
    pass


class EnumLookupError(Exception):
    """
    Raised when an enum cannot be found by the specified method of lookup.
    """
    pass


class EnumComparisonWarning(Warning):
    """
    Raised when comparing an enum to a value of another type.
    """
    pass


class EnumValue(object):
    def __init__(self, index, value):
        self.value = value
        if index < 0:
            raise EnumConstructionException("Index cannot be a negative number")
        self.index = index

    def __repr__(self):
        return "{0} index: {1} value: {2}".format(self.__class__.__name__,
                                                  self.index,
                                                  self.value)

    def __str__(self):
        return self.value

    def __hash__(self):
        return hash(self.index)

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, type(other)):
            return False
        return self.index == other.index

    def __ne__(self, other):
        return not (self.__eq__(other))


class RichEnumValue(object):
    def __init__(self, canonical_name, display_name):
        self.canonical_name = canonical_name
        self.display_name = display_name

    def __unicode__(self):
        return self.display_name

    def __repr__(self):
        return "{0} - canonical_name: '{1}' display_name: '{3}'"  .format(self.__class__.__name__,
                                                                          self.canonical_name,
                                                                          self.display_name)

    def __str__(self):
        return self.display_name

    def __hash__(self):
        return hash(self.canonical_name)

    def __cmp__(self, other):
        if other is None:
            return -1
        if not isinstance(other, type(self)):
            return -1
        return __cmp__(self.canonical_name, other.canonical_name)

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, type(self)):
            return False
        return self.canonical_name == other.canonical_name

    def __ne__(self, other):
        return not (self.__eq__(other))


class OrderedRichEnumValue(RichEnumValue):
    def __init__(self, index, canonical_name, display_name):
        super(OrderedRichEnumValue, self).__init__(canonical_name, display_name)
        if not isinstance(index, int):
            raise EnumConstructionException("Index must be an integer type, not: {0}".format(type(index)))
        if index < 0:
            raise EnumConstructionException("Index cannot be a negative number")
        self.index = index

    def __repr__(self):
        return "{0} - index: {1}  canonical_name: '{2}'  display_name: '{3}'".format(self.__class__.__name__,
                                                                                     self.index,
                                                                                     self.canonical_name,
                                                                                     self.display_name)

    def __str__(self):
        return "{0}"

    def __cmp__(self, other):
        if other is None:
            return -1
        if not isinstance(other, type(self)):
            return -1
        return __cmp__(self.index, other.index)

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, type(self)):
            return False
        return self.index == other.index
