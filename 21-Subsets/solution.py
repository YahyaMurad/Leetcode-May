class Solution:
    def subsets(self, nums):
        n = 2 ** len(nums)

        res = []
        for counter in range(0, n):
            arr = []
            for j in range(0, len(nums)): 
                if (counter & (1 << j)) > 0: 
                    arr.append(nums[j])
            res.append(arr)

        return res