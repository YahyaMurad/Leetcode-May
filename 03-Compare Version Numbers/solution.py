class Solution:
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        for one, two in zip(v1, v2):
            if int(one) < int(two):
                return -1
            elif int(one) > int(two):
                return 1
        if len(v1) == len(v2):
            return 0
        elif len(v1) < len(v2):              
            for i in range(len(v1), len(v2)):
                if v2[i] > 0:
                    return -1
        elif len(v1) > len(v2):
            for i in range(len(v2), len(v1)):
                if v1[i] > 0:
                    return 1
        
        return 0

sol = Solution()
print(sol.compareVersion("1.0", "1.0.0"))