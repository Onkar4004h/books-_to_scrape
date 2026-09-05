def find_max(nums):
    if len(nums)==1:
        return nums[0]
    else:
        max_of_rest=find_max(nums[1:])
        return nums[0] if nums[0]>max_of_rest else max_of_rest
print(find_max([9,3,2,4,8]))
