def concat_array(nums):
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums


print(concat_array([1, 2, 1]))
