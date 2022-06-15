"""
Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order,
and in which the subsequence is as long as possible.
This subsequence is not necessarily contiguous, or unique.
In this case, we only care about the length of the longest increasing subsequence.

Input Format:
The first and the only argument is an integer array A.
Output Format:

Return an integer representing the length of the longest increasing subsequence.
Constraints:

1 <= length(A) <= 2000
0 <= A[i] <= 2500
Example :
Input 1:
    A = [1, 2, 1, 5]
Output 1:
    3
Explanation 1:
    The sequence : [1, 2, 5]
Input 2:
    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output 2:
    6
Explanation 2:
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
"""

from bisect import insort, bisect_left, bisect_right


def count_bigger_number(data):
    if len(data) == 1:
        result = 0
    else:
        data_to_check = data[0]
        lis_data = data[1:].copy()
        number = 0
        for i, num in enumerate(lis_data):
            if num > data_to_check:
                number += 1
        result = number

    return result


def longest_increasing_subsequence(A):

    if not A:
        result = 0
    elif len(A) == 1:
        result = 1
    else:
        aux_lis = A
        continue_iterating = True
        biggest_subsequence = []
        while continue_iterating:
            number_bigger_numbers_max = 0
            element_index_to_add = len(aux_lis) - 1
            for i, data in enumerate(aux_lis):
                number_bigger_numbers = count_bigger_number(aux_lis[i:])
                if number_bigger_numbers > number_bigger_numbers_max and (aux_lis[i] not in biggest_subsequence) and \
                        (biggest_subsequence == [] or aux_lis[i] > biggest_subsequence[-1]):
                    element_index_to_add = i
                    number_bigger_numbers_max = number_bigger_numbers

            biggest_subsequence.append(aux_lis[element_index_to_add])

            if (element_index_to_add == (len(aux_lis) - 1)):
                continue_iterating = False
            else:
                aux_lis = aux_lis[(element_index_to_add + 1):]

        result = len(biggest_subsequence)
        print(biggest_subsequence)

    return result


# Program answer
def lis(A):
    d = [A[0]]
    n = len(A)
    for i in range(1, n):
        if d[-1] < A[i]:
            d.append(A[i])
        else:
            idx = bisect_left(d, A[i])
            d[idx] = A[i]

    print(d)
    return len(d)


test_list = [69, 54, 19, 51, 16, 54, 64, 89, 72, 40, 31, 43, 1, 11, 82, 65, 75, 67, 25, 98, 31, 77, 55, 88, 85, 76, 35,
              101, 44, 74, 29, 94, 72, 39, 20, 24, 23, 66, 16, 95, 5, 17, 54, 89, 93, 10, 7, 88, 68, 10, 11, 22, 25, 50,
              18, 59, 79, 87, 7, 49, 26, 96, 27, 19, 67, 35, 50, 10, 6, 48, 38, 28, 66, 94, 60, 27, 76, 4, 43, 66, 14, 8,
              78, 72, 21, 56, 34, 90, 89]
biggest_subsequence_lon_editorial = lis(test_list)
biggest_subsequence_lon = longest_increasing_subsequence(test_list)
print(biggest_subsequence_lon)
print(biggest_subsequence_lon_editorial)

