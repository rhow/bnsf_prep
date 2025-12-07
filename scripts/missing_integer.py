
def Solution(A):

    n = len(A)
    i = 0

    while i < n:
        current_val = A[i]
        correct_index = current_val - 1

        if 1 <= current_val <= n and current_val != A[correct_index]:
            # Swap A[i] with the number at its correct_index
            A[i], A[correct_index] = A[correct_index], A[i]

        else:
            i += 1

    for i in range(n):
        # The first index 'i' where the value is not 'i + 1' is the missing number.
        if A[i] != i + 1:
            return i + 1
        
    return n + 1

# a = [1, 1, 4, 3, 2, 6]
# a = [-1, -3]
a = [1, 2, 100]
print(a)

results = Solution(A=a)

print(results)