class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maximum =0
        stack = [-1]
        index=0
        for i , char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maximum = max(i-stack[-1] , maximum)
                else:
                    stack.append(i)
        return maximum