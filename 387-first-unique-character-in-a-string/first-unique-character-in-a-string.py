class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for i in range(len(s)):
        #     if s[i] not in s[i+1:] and s[i] not in s[:i]:
        #         return i
            
        # return -1
        hash_map = {}
        for i in s:
            hash_map[i]  = hash_map.get(i , 0)+1
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1