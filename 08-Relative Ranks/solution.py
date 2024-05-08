class Solution:
    def findRelativeRanks(self, score):
        arr = score.copy()
        arr.sort(reverse=True)

        h = {}
        n = 1
        for i in arr:
            if n < 4:
                h[i] = "Gold Medal" if n == 1 else "Silver Medal" if n == 2 else "Bronze Medal"
            else:
                h[i] = str(n)

            n += 1
        
        res = []
        for i in score:
            res.append(h[i])

        return res
