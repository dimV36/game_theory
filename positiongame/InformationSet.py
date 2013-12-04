__author__ = 'dimv36'


class InformationSet:
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = list(nodes)

    def __str__(self):
        return "InformationSet\n{0}, {1}".format(self.name, self.nodes)

    def __repr__(self):
        return "{0}, {1}".format(self.name, self.nodes)

    def __eq__(self, other):
        return self.name == other.name and self.nodes == other.nodes

    def __ne__(self, other):
        return not self.__eq__(other)

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def count(self):
        return len(self.nodes)