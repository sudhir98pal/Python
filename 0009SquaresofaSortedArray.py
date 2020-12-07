# Q link->https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0 for i in range(0,n)]
        i=n-1
        l,r=0,n-1
        while l<=r:
            x,y=nums[l]*nums[l],nums[r]*nums[r]
            if x>=y:
                ans[i]=x
                i-=1
                l+=1
            else:
                ans[i]=y
                i-=1
                r-=1
        return ans
        
