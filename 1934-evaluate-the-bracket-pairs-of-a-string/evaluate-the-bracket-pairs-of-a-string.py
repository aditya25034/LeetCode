class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hash_map = {key : value for key, value in knowledge}
        i = 0
        n = len(s)
        res =[]
        while i<n:
            if s[i] == "(":
                j = i+1
                while j < n and s[j] != ")":
                    j+=1
                
                key = s[i+1 : j]
                res.append(hash_map.get(key , "?"))

                i=j+1
            else:
                res.append(s[i])
                i+=1

        return "".join(res)