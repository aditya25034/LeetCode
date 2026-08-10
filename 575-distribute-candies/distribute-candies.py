class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n= len(candyType)
        hash_set = set(candyType)
        if len(hash_set) < n//2:
            return len(hash_set)
        return n//2