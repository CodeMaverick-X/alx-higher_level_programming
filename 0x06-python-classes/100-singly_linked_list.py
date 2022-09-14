#!/usr/bin/python3
"""a class Node that defines a node of a singly linked list"""


class Node:
    """a class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """instantiation of object atrr"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter method for the data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter to retrieve the next nonde"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for the net_node attribute"""
        if isinstance(value, Node) or isinstance(value, None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """class to represwnt the singlu linked list"""

    def __init__(self):
        """instantiation"""
        self.__head = None

    def __str__(self):
        """for print statement"""
        my_str = ""
        node = self.__head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        """sorted insert into the list"""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        ptr = self.__head
        while ptr.next_node and ptr.next_node.data < value:
            ptr = ptr.next_node
        new_node.next_node = ptr.next_node
        ptr.next_node = new_node
