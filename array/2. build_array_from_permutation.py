def build_array_from_permutation(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(nums[nums[i]])
    return ans


print(build_array_from_permutation([0, 2, 1, 5, 3, 4]))
