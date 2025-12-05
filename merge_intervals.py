
# [[1, 3], [2, 6], [8, 10], [15, 18]] to [[1, 6], [8, 10], [15, 18]]

input_intervals = [[1, 3], [2, 6], [8, 16], [15, 18]]
input_intervals = sorted(input_intervals)
print(f"Original input intervals: {input_intervals}")


def merge_intervals(interval_1: list[int, int], interval_2: list[int, int]) -> list[bool, list[int, int]]:
    # Assumes minimum of interval_1 is less than/equal to minimum of interval_2
    merged = False

    lower_bound = min(interval_1)
    # Test if the maximum of the 1st is greater than/equal to maximum of 2nd
    # 1 completely includes 2
    if max(interval_1) >= max(interval_2):
        merged = True
        upper_bound = max(interval_1)
        return [merged, [lower_bound, upper_bound]]

    upper_bound = max(interval_1)
    # Test if maximum of 1st is more than/equal to minimum of 2nd
    # 1 partially overlaps 2
    if max(interval_1) >= min(interval_2):
        merged = True
        upper_bound = max(interval_2)

    return [merged, [lower_bound, upper_bound]]


modified = True
while modified:
    modified = False
    merged_intervals = []
    skip_next_interval = False
    i_count = len(input_intervals)

    # Iterate over the elements excluding the last one
    for idx in range(i_count - 1):

        # This interval might have been merged into the previous, skip it
        if skip_next_interval:
            skip_next_interval = False
            continue

        current_interval = input_intervals[idx]
        next_interval = input_intervals[idx + 1]

        # Potentially merge the intervals
        merged, new_interval = merge_intervals(current_interval, next_interval)

        if merged:
            # Append the new merged interval to the output
            merged_intervals.append(new_interval)
            # Indicate the next interval has been merged and the list has been modified
            skip_next_interval = True
            modified = True
        
        else:
            # Not merged, add both to the output
            merged_intervals.append(current_interval)
            merged_intervals.append(next_interval)
    
    if modified:
        # Input has been modified, update the processing input list to the new merged interval list
        input_intervals = merged_intervals


print(f"Final merged intervals: {merged_intervals}")
