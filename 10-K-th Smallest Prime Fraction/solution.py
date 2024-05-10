class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        fractions = []

        for i in range(len(arr)):
            for j in range(len(arr)):
                fractions.append([[arr[i], arr[j]], arr[i] / arr[j]])

        fractions.sort(key=lambda x: x[1])

        return fractions[k][0]

sol = Solution()
print(sol.kthSmallestPrimeFraction([1, 2, 3, 5], 2))