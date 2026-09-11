def find_pivot_index(nums):
    total=sum(nums)
    left_sum=0
    for i in range(len(nums)):
        right_sum=total-left_sum-nums[i]
        if left_sum==right_sum:
            return i
        left_sum+=nums[i]
    return -1
print(find_pivot_index([2,1,-1]))     