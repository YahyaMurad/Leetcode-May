class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = len(nums)
        counter = 0
        while x != 0:
            counter = 0
            for num in nums:
                if num >= x:
                    counter += 1
            if counter == x:
                return x
            x -= 1
            
        return -1