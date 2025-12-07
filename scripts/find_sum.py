
def find_sum(nums: list[int], target: int) -> list[int]:
    
    val_idxs = {}
    for idx in range(len(nums)):

        diff = target - nums[idx]

        if diff in val_idxs:
            return [val_idxs[diff], idx]

        val_idxs[nums[idx]] = idx

    return []

inputs = [0,1,4,6,8]
# print("inputs", inputs)

results = find_sum(inputs, target=9)
print(results)