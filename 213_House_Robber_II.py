class Solution:
    def rob(self, nums: List[int]) -> int:
        
        length = len(nums)
        if length == 1: return nums[0]
        self.d = {}
        ans =  self.dp(nums,0,length-1)
        self.d = {}
        ans =  max(self.dp(nums,1,length),ans)
        ans =  max(self.dp(nums,2,length),ans)
        
        return ans

    def dp(self, nums, ind,length):
        if ind < length:
            if ind in self.d: return self.d[ind]
            self.d[ind] = max(self.dp(nums,ind+2,length),self.dp(nums,ind+3,length))
            self.d[ind] += nums[ind]
            return self.d[ind]
        return 0
