class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        n=len(s)
        vowel_count =0
        vowels = {"a" , "e" ,"i" , "o" ,"u"}
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        ans = vowel_count
        for i in range(k,n):
            if s[i] in vowels:
                vowel_count+=1
            if s[i-k] in vowels:
                vowel_count -=1
            ans = max(ans , vowel_count)
        return ans
        