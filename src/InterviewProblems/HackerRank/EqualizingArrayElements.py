def NeedeOperationsNumbers(FinalNumber, SourceNumber, divisor):
    num_op = 0
    flag = False
    if SourceNumber == FinalNumber:
        return num_op
    while int(SourceNumber) > FinalNumber:
        SourceNumber /= divisor
        num_op += 1
        if (int(SourceNumber) == FinalNumber):
            flag = True
            break
    if flag:
        return num_op
    else:
        return None


def minOperations(arr, threshold, d):
    # Write your code here
    aux_array = []
    arr.sort()
    for i, data in enumerate(range(arr[len(arr) - 1] + 1)):
        if (arr.count(data) >= threshold):
            return 0
        larger_elements = [element for element in arr if element > (data * d)]
        num_possible_equal = len(larger_elements)
        if (num_possible_equal < threshold):
            aux_array.append(None)
            continue
        number_operations = []
        for i, arr_data in enumerate(arr):
            if arr_data < data:
                number_operations.append(None)
            else:
                ned_op = NeedeOperationsNumbers(data, arr_data, d)
                number_operations.append(ned_op)

        number_operations = [i for i in number_operations if i]
        if len(number_operations) >= threshold:
            number_operations.sort()
            aux_array.append(sum(number_operations[:threshold]))
        else:
            aux_array.append(None)

    aux_array = [i for i in aux_array if i]
    aux_array.sort()

    return aux_array[0]

arr = [3,3,3,3,3]
result = minOperations(arr, 2, 3)
print(result)
