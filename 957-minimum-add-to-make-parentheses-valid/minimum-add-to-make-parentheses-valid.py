class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opencount = 0
        closecount =0
        res = 0
        for i in s:
            if i=="(":
                opencount +=1
            else:
                if opencount:
                    opencount -= 1
                
                else:
                    res +=1
        return res + opencount

