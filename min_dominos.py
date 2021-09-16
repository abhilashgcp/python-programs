from __future__ import annotations
class Solution:
    def minDominoRotation (self, A: List[int], B: List[int]) -> int:
        top_a = self.helper (A, B, A[0])
        top_b = self.helper (A, B, B[0])
        btm_a = self.helper (B, A, A[0])
        btm_b = self.helper (B, A, B[0])
        minimum = min (top_a, btm_a, top_b, btm_b)
        return -1 if  minimum == 40000 else minimum
    def helper (self, top: List[int] , bottom: List[int], match: int) -> int:
        count =0
        for i in range(len(top)):
            if (top[i] != match):
                if (bottom[i] == match):
                    count +=1
                else:
                    return 40000
        return count


A=[2,1,2,4,2,2]
B=[5,2,6,2,3,2]

Sln = Solution()
print (Sln.minDominoRotation(A,B))
