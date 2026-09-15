class Solution:
    def secondHighest(self, s: str) -> int:
        lst = [ int(i) for i in s if i.isdigit()]

        largest = float("-inf")
        second = float("-inf")
        for i in lst:
            if i > largest:
                largest = i
        for i in lst:
            if i > second and i!= largest:
                second = i
        if second >= 0:
            return second
        return -1
        