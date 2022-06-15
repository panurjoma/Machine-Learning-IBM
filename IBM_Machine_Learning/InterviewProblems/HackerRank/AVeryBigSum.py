"""
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that
some of those integers may be quite large.
Function Description
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
aVeryBigSum has the following parameter(s):
int ar[n]: an array of integers .
Return
long: the sum of all array elements
Input Format
The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.
Output Format
Return the integer sum of the elements in the array.
"""

def aVeryBigSum(ar):
    # Write your code here
    ar.sort()

    if len(ar) == 1:
        return ar[0]

    b = ar[0]
    num_common = ar[0] * len(ar)
    ar = list(map(lambda x: x - b, ar))
    num_sum = aVeryBigSum(ar[1:]) + num_common

    return num_sum

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = aVeryBigSum(ar)
print(result)
