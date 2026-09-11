def running_sum_1d(nums):
    sum_array=[]
    sum_array.append(nums[0])
    l=1
    r=0
    while l<len(nums):
        sum=nums[l]+sum_array[r]
        sum_array.append(sum)
        l+=1
        r+=1
    return sum_array
print(running_sum_1d( [3,1,2,10,1]))      