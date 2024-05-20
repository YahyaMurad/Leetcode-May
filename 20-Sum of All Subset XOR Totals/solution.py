import math

class Solution:
    def sumXOR(self, nums):
        if nums:
            res = nums[0]
            for i in range(1, len(nums)):
                res ^= nums[i]

            return res
        
        return 0
    
    def printPowerset(self, nums):
        set_size = len(nums)
        pow_set_size = (int) (math.pow(2, set_size))
        counter = 0
        j = 0

        res = 0

        for counter in range(0, pow_set_size):
            arr = []
            for j in range(0, set_size): 
                if (counter & (1 << j)) > 0: 
                    arr.append(nums[j])
            res += self.sumXOR(arr)

        return res

    def subsetXORSum(self, nums):
        return self.printPowerset(nums)
