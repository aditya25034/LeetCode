class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        hash_map = {")" : "(" , "}" : "{" ,"]":"[" }
        for i in s:
            if not stack and (i == ")" or i== "}" or i == "]"):
                return False
            if i == "(" or i== "{" or i == "[":
                stack.append(i)
            elif hash_map[i] == stack.pop():
                pass
            else:
               return False

        if stack:
            return False
        return True

            