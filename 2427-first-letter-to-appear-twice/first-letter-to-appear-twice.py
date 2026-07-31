class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans=""
        lst = [0]*26
        for ch in s:
            x = ord(ch)-97
            if lst[x]<2:
                lst[x] +=1
                if lst[x]==2:
                    ans =ch
                    return ans