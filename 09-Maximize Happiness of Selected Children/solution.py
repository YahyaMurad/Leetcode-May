class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)

        res = 0
        counter = 0
        for i in range(min(k, len(happiness))):
            res += max(0, happiness[i] - counter)
            counter += 1
        
        return res
