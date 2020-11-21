class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f=-1
        s=nums[0]
        for i in range(len(nums)):
            if(nums[i]>s):
                return True
            if(nums[i]>f):
                f=nums[i]
            if(nums[i]>f):
                s=nums[i]
        return False        
            
        
