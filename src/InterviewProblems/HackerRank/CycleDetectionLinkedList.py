#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    linked_list = []
    while node:
        node = node.next

        if node:
            linked_list.append(node.data)

    print(linked_list)


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    node_list = []
    current = head
    flag_cycle = 0
    while current.next != None:
        node_list.append(current)
        current = current.next
        if current in node_list:
            flag_cycle = 1
            break

    return flag_cycle


if __name__ == '__main__':

    llist = SinglyLinkedList()

    for data in range(9):
        llist_item = data
        llist.insert_node(llist_item)

    llist.head.next.next.next = llist.head.next

    list_with_cycle = has_cycle(llist.head)

    print(list_with_cycle)

