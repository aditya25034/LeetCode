class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index =0
        s=s.strip()
        for i in range(len(s)-1 , -1, -1):
            if s[i] == " ":
                index = i+1
                break
        return len(s[index:])