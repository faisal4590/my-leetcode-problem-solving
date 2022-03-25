def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break
        if len(result) > 0:
            break
    return result


# print(twoSum([3, 4, 6], 10))
