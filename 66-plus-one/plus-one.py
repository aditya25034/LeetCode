class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num =0
        for i in digits:
            num = (num*10)+i
        num+=1

        arr=[]
        
        while num>0:
            a=num%10
            num =num//10
            arr.append(a)
                    
        l=0
        r=len(arr)-1
        while l<r:
            arr[l], arr[r]= arr[r], arr[l]
            l+=1
            r-=1
        return arr