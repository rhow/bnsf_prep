def merge_intervals_efficient(intervals: list[list[int]]) -> list[list[int]]:
    # Handle edge case for empty or single-element list
    if not intervals:
        return []

    # 1. Sort the intervals by their start time. O(N log N)
    intervals.sort(key=lambda x: x[0])
    
    # Initialize the result list with the first interval
    merged_intervals = [intervals[0]]
    
    # 2. Iterate through the remaining intervals (starting from the second one)
    for current_start, current_end in intervals[1:]:
        
        # Get the last merged interval from the result list
        _, last_merged_end = merged_intervals[-1]
        
        # Check for overlap: If the current interval's start is less than or equal 
        # to the end of the last merged interval.
        if current_start <= last_merged_end:
            # Overlap exists: Merge by extending the last merged interval's end time
            # The start remains the same (since the list is sorted)
            new_end = max(last_merged_end, current_end)
            merged_intervals[-1][1] = new_end
        else:
            # No overlap: Add the current interval to the result list
            merged_intervals.append([current_start, current_end])
            
    return merged_intervals


# Your input (fixed for the example)
input_intervals = [[1, 3], [2, 6], [8, 16], [15, 18]]
result = merge_intervals_efficient(input_intervals)

print(f"Input intervals: {input_intervals}") 
print(f"Final merged intervals: {result}")