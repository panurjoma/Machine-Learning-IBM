"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.
Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example.
The two flavors that cost  and  meet the criteria. Using -based indexing, they are at indices  and .
Function Description
Complete the icecreamParlor function in the editor below.
icecreamParlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
Input Format

The first line contains an integer, , the number of trips to the ice cream parlor. The next  sets of lines each describe a visit.
Each trip is described as follows:

The integer , the amount of money they have pooled.
The integer , the number of flavors offered at the time.
 space-separated integers denoting the cost of each flavor: .
Note: The index within the cost array represents the flavor of the ice cream purchased.
"""


def icecreamParlor(m, arr):
    # Write your code here
    index_result = []
    num_combinations = int(m / 2)
    first_number = 1
    for i in range(num_combinations):
        second_number = m - first_number
        if (first_number in arr) and (second_number in arr):
            if (arr.index(first_number) != arr.index(second_number)):
                index_result.append(arr.index(first_number) + 1)
                index_result.append(arr.index(second_number) + 1)
            else:
                index_result = [index for index, char in enumerate(arr) if char == first_number]
                index_result[0] += 1
                index_result[1] += 1
            break
        else:
            first_number += 1

    index_result.sort()
    return index_result


prices = [2, 2, 4, 3]
money = 4
selected = icecreamParlor(money, prices)
print(selected)
