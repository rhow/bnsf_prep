

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # 0. Edge case if intervals is null/empty
    if not intervals:
        return []     
    
    # Define constant for the end index of the interval
    _IDX_START = 0
    _IDX_END = 1

    # 1. Inplace sort on the first element of each interval
    intervals.sort(key=lambda x: x[_IDX_START])

    # 2. Initialize the results with the first interval
    merged_intervals = [intervals[0]]

    # 3. Iterate over the intervals starting at the 2nd element
    for current_interval in intervals[1:]:

        # Compare the current start and the last end values
        if current_interval[_IDX_START] <= merged_intervals[-1][_IDX_END]:
            # If the current start value is less than/equal use the higher end value
            merged_intervals[-1][_IDX_END] = max(merged_intervals[-1][_IDX_END],
                                                 current_interval[_IDX_END])
        
        else:
            # Otherwise append the current interval to the merge list
            merged_intervals.append(current_interval)
    
    return merged_intervals

intervals = [[2, 6], [1, 3], [8, 17], [9, 10], [14, 15], [16, 18], [19, 21]]
print(f"Intervals: {intervals}")

results = merge_intervals(intervals)
print(f"Results: {results}")
