#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
    
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if self.__next_node is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        
    def __str__(self):
        return(f"You entered the value {self.__data} and {self.__next_node}")


a = Node(1,1)
b = Node(5,6)
print(a)
# a.data = "30"
# print(a.data)

# class SinglyLinkedList:
#     def __init__(self, head):
#         self.__head = head

#     def sorted_insert(self, value):



    
# sll = SinglyLinkedList()
# sll.sorted_insert(2)
# sll.sorted_insert(5)
# sll.sorted_insert(3)
# sll.sorted_insert(10)
# sll.sorted_insert(1)
# sll.sorted_insert(-4)
# sll.sorted_insert(-3)
# sll.sorted_insert(4)
# sll.sorted_insert(5)
# sll.sorted_insert(12)
# sll.sorted_insert(3)
# print(sll)
