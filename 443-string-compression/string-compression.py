class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        ans = ""
        for i in range(len(chars)-1):
            if chars[i+1] == chars[i]:
                count +=1
            else:
                ans += chars[i]
                if count >1:
                    ans += str(count)
                    
                count = 1
            
        ans+=chars[-1]
        if count>1:
            ans+= str(count)
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)
