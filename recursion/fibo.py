def fiboseries(target_index):
    nums = [0,1]
    while len(nums)<target_index:
        r = len(nums)-1
        y = nums[r]+nums[r-1]
        nums.append(y)
    return nums[-1]
# print(fiboseries(5)) 

def fiboRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fiboRec(n-1) + fiboRec(n- 2)

print(fiboRec(6))