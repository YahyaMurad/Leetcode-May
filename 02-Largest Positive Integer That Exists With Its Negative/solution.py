class Solution:
    def findMaxK(self, nums):
        ans = -1
        for num in nums:
            if num > 0 and -num in nums:
                ans = max(ans, num)
        
        return ans