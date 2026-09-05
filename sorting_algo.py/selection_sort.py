def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                nums[j],nums[min_index]=nums[min_index],nums[j]

    return nums 
def bubble_sort(nums):
    n=len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums            
print(bubble_sort([5, 3, 4, 1, 2]))                           

        

