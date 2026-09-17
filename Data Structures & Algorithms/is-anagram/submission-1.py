class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i],0) + 1
        tMap = {}
        for j in range(len(t)):
            tMap[t[j]] = tMap.get(t[j], 0 ) + 1
        if sMap != tMap:
            return False 
        return True  