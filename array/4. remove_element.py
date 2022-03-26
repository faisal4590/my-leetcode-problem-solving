"""
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 2.
    It does not matter what you leave beyond the returned k (hence they are underscores).
"""

"""
    array traverse korte chaile always last theke start korbo to avoid index out of bound problem.
"""


def remove_elements_from_array(nums, val):
    n = len(nums)
    for i in range(n):
        idx = n - i - 1
        if nums[idx] == val:
            del nums[idx]
    return len(nums)


print(remove_elements_from_array([0, 1, 2, 2, 3, 0, 4, 2], 2))
