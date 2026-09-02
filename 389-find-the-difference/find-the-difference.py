class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i=0
        hash_map={}
        for i in range(len(t)):
            hash_map[t[i]] = hash_map.get(t[i] ,0)+1
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i] ,0)-1
        ans = next(k for k, v in hash_map.items() if v == 1)
        return ans
        