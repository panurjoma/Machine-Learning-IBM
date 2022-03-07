
# Function to calculate the maximum
# possible value at index K
def maxValueAtIndexK(N, K, M):
    # Stores the sum of elements
    # in the left and right of index K
    S1 = K * (K + 1) // 2
    S2 = (N - K - 1) * (N - K) // 2

    # Stores the maximum
    # possible value at index K
    X = (M + S1 + S2) // N

    # Prthe answer
    return X


result = maxValueAtIndexK(3, 1, 7)
print(result)
