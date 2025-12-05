
def firstMissingPositive(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    print(f"--- Starting List: {nums} (N={n}) ---")

    # 1. In-Place Hashing (Swapping)
    while i < n:
        current_val = nums[i]
        correct_index = current_val - 1

        # Check conditions for a valid swap:
        # 1. The value is a positive number (1 <= current_val)
        # 2. The value belongs within the list's indices (current_val <= n)
        # 3. The value is NOT already in its correct position (nums[i] != nums[correct_index])
        if 1 <= current_val <= n and current_val != nums[correct_index]:
            # --- Print BEFORE the swap ---
            print(f"\n[i={i}] Current list: {nums}")
            print(f"  --> Swapping value {current_val} (at index {i}) with {nums[correct_index]} (at index {correct_index})")
            
            # Perform the swap
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
            
            # --- Print AFTER the swap ---
            print(f"  <-- After swap: {nums}")
            # Note: i is NOT incremented, as we need to re-check the new value at nums[i]
        else:
            print(f"[i={i}] Current value {nums[i]} (i increments, no swap)")

            # No swap needed (number is negative, out of range, or already correct)
            i += 1
            
    # 2. Find the First Mismatch
    print(f"\n--- Final Rearranged List: {nums} ---")
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
            
    # 3. Handle Edge Case: All numbers 1 to N are present
    return n + 1

# l = [-3, -1, 0, 1, 2, 4]
l = [-3, -2, -1, 0]
result = firstMissingPositive(l)
print(f"\nRESULT: The first missing positive number is: {result}")
