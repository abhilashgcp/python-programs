from __future__ import annotations
from heapq import heapify,heappop

class solution:
    def findKthLargest(self, k:int, nums: List[int]) -> int:
        is_min_heap = (len(nums)-k+1) < k #Use min heap
        k_largest = None
        if (is_min_heap):
            print ("Using Min heap")
            nums = [(num,num) for num in nums]  
        else:
            print ("Using Max heap")
            nums = [(-num,num) for num in nums]
        heapify (nums)
        
        if (is_min_heap):
           for _ in range(len(nums)-k):
               heappop(nums)
           k_largest = heappop(nums)[len(nums)-k]
        else:
            for _ in range(k-1):
                heappop(nums)
            k_largest = heappop(nums)[1]
        return k_largest

sln = solution()
print (sln.findKthLargest(2,[8,1,3,2,6,7]))
print (sln.findKthLargest(5,[8,1,3,2,6,7]))
