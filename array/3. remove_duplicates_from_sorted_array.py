"""
    right pointer diye ami amar array ta scan korbo. jodi new kono value pai tahole left pointer e oita boshay dibo.
    suppose input = [0 , 0, 1, 1]
    left_pointer = 1 (arr[1] ke point korce)
    right pointer = 1 (arr[1] ke point korce)
    now bujhbo kivabe je new element paici?
    as right_pointer diye scan korteci, so right_pointer er previous value ta jodi current er same na hoy tar mane new value paici

    if(arr[right_pointer] != arr[right_pointer - 1])
    {
        arr[left_pointer] = arr[right_pointer]
        left_pointer += 1
    }
"""


def remove_duplicate_from_sorted_array(nums):
    left_pointer = 1  # we don't need to check the 1st index

    for right_pointer in range(1, len(nums)):
        if nums[right_pointer] != nums[right_pointer - 1]:
            nums[left_pointer] = nums[right_pointer]
            left_pointer += 1
    return left_pointer


print(remove_duplicate_from_sorted_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
