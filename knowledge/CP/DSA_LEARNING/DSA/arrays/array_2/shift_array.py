nums = [10,20,30,40,50,60]
def shift_array(nums, shift_value: int):
    shift_value = -shift_value
    if shift_value < 0:
        shift_value = len(nums) + shift_value
    temp_arr = nums[shift_array:]
    del nums[shift_array:]
    main_arr = temp_arr + nums
    return main_arr

arr = shift_array(nums=nums, shift_value=3)
print(arr)