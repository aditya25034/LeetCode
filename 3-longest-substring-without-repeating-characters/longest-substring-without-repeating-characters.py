class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest =0
        curr =0
        hash_map = {}
        n=len(s)
        i=0
        while i<n:
            if s[i] in hash_map:
                x=hash_map[s[i]]
                curr =0
                hash_map.clear()
                i = x+1
                
            else:
                hash_map[s[i]] = i
                curr+=1
                longest = max(curr , longest)
                i+=1
            
        return longest