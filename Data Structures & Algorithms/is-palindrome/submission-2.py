
class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=''
        num=0
        for i in range(len(s)):
            if s[i].isalnum():
                k+=s[i]
                num+=1
        i = 0
        j = len(k)-1
        while(i<j):
            if k[i].lower() == k[j].lower() :
                i+=1
                j-=1
                
            else:
                return False
        return True
        