class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map1 ={}
        hash_map2 = {}
        for i in ransomNote:
            hash_map1[i] = hash_map1.get(i , 0)+1
        for i in magazine:
            hash_map2[i] = hash_map2.get(i , 0)+1
        for i in ransomNote:
            if (i not in hash_map2) or (hash_map2[i] < hash_map1[i]):
                return False
        return True
                