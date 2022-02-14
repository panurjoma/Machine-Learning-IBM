"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if
left rotations are performed on array , then the array would become . Note that the lowest index item moves to the
 highest index in a rotation. This is called a circular array.
Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be
 printed as a single line of space-separated integers.
Function Description
Complete the function rotLeft in the editor below.
rotLeft has the following parameter(s):
int a[n]: the array to rotate
int d: the number of rotations
Returns
int a'[n]: the rotated array
Input Format
The first line contains two space-separated integers  and , the size of  and the number of left rotations.
The second line contains  space-separated integers, each an .
"""


# -- Recursion version -- #
def rotLeft1(a, d):
    # Write your code here
    if len(a) == 1:
        return a

    # new_array = a[1:] + [a[0]]
    a.append(a.pop(0))

    if d == 1:
        return a

    new_array = rotLeft1(a, d - 1)

    return new_array


# -- without recursion -- #
def rotLeft2(a, d):
    # Write your code here
    if len(a) == 1:
        return a

    if d > len(a):
        d = d - (int(d / len(a)) * len(a))

    new_array = a[d:] + a[0:d]

    return new_array

list_to_rotate = [1, 2, 3, 4, 5]
rotated_list = rotLeft2(list_to_rotate, 4)
print(rotated_list)