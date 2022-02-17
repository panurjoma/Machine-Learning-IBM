"""
In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same
approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array,
 one element at a time? Note that in the first step, when you consider an array with just the first element, it is
  already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been
 inserted at its correct position. Since the array composed of just the first element is already sorted, begin
  printing after placing the second element.

Example.

Working from left to right, we get the following output:

3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7
Function Description

Complete the insertionSort2 function in the editor below.
insertionSort2 has the following parameter(s):
int n: the length of
int arr[n]: an array of integers
Prints

At each iteration, print the array as space-separated integers on its own line.
"""


def insertionsort1(n, arr):
    index = 0
    while (index < len(arr) and n > arr[index]):
        index += 1

    temp_array = arr[0:index] + [n] + arr[index:]

    return temp_array


def insertionSort2(n, arr):
    # Write your code here
    temp_array = [arr[0]]
    index = 1
    while (index < n):
        temp_array = insertionsort1(arr[index], temp_array)
        print(*(temp_array + arr[(index + 1):]), sep=' ')
        index += 1

n = 6
arr = [1, 4, 3, 5, 6, 2]
insertionSort2(n, arr)