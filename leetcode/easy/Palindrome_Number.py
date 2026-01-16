class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = [int(d) for d in str(x)]
        l=len(num)
        j=l-1
        for i in range(0,(l//2)):
            if num[i]!=num[j]:
                return False
            j = j-1
        return True        
    
   
            
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]  