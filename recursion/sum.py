def sum_list(nums):
    if len(nums)==0:
        return 0
    else:
        return nums[0]+sum_list(nums[1:])
        

print(sum_list([1, 2, 3, 4, 5]))    