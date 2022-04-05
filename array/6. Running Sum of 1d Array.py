def sum_of_running_1d_array(nums):
    runningSum = []
    for i in range(len(nums)):
        sum = 0
        for j in range(0, i + 1):
            sum += nums[j]
        runningSum.append(sum)
    return runningSum


print(sum_of_running_1d_array([3, 1, 2, 10, 1]))
