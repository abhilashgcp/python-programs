def FindPeak(nums):
    left = 0
    right = len(nums) -1
    while (left < right):
        mid = left + (right-left)//2
        if (nums[mid] < nums[mid+1]):
            left = mid + 1
        else:
            right = mid
    return left

a = [1,2,1,3,5,6,4]
print (FindPeak(a))