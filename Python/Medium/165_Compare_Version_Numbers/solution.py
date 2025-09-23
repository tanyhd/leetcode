class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        maxLength = max(len(v1), len(v2))

        if len(v1) < maxLength:
            v1 += ["0"] * (maxLength - len(v1))
        
        if len(v2) < maxLength:
            v2 += ["0"] * (maxLength - len(v2))
        
        
        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            if int(v1[i]) > int(v2[i]):
                return 1
        
        return 0