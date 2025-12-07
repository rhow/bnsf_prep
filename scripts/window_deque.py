from collections import deque 


def sliding_window_sum(arr: list[int], k: int) -> list[int]:
    """
    Calculates the sum of all elements in a sliding window of size k.
    This method maintains O(N) complexity overall.
    """
    if not arr or k <= 0 or k > len(arr):
        return []

    results = []
    
    # Initialize the deque to store the first window's elements (or indices)
    # Here, we'll use the deque to store the values for clarity.
    window = deque()

    # Iterate through the array
    for i, value in enumerate(arr):
        
        # 1. ADD New Element (O(1) operation)
        window.append(value)

        # 2. CHECK Window Size
        if i >= k - 1:
            # The window is full (or has passed its initial size)
            # Record the result for the current window
            results.append(max(window))
            
            # 3. DROP Oldest Element (O(1) operation)
            # Find the element that is exiting the window (at the front/left)
            _ = window.popleft()
    
    return results

nums = [2, 1, 5, 2, 3]
k = 3

results = sliding_window_sum(nums, k=k)
print(results)
