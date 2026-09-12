def sumarray_sum_equal_k(nums,k):
    prefix={0:1}
    prefix_sum=0
    answer=0
    for num in nums:
        prefix_sum+=num
        needed=prefix_sum-k
        if needed in prefix:
            answer+=prefix[needed]
        prefix[prefix_sum]=prefix.get(prefix_sum,0)+1
    return answer
print(sumarray_sum_equal_k([1,2,3],3))       
