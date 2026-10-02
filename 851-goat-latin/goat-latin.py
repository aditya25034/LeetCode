class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "AEIOUaeiou"
        lst = sentence.split()
        count=0
        for i in lst:
            if i[0] not in vowels:
                temp = i[0]
                i = i[1:] + i[0] 
            
            i = i+"ma" 
            lst[count] =i
            count+=1

        count =1
        while count<=len(lst):
            lst[count-1] = lst[count-1] + ("a" * count)
            count +=1

        return (" ".join(lst))
