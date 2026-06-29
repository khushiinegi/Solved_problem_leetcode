class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x 
        rev = 0
        while x > 0 :
            dig = x % 10
            rev = rev * 10 + dig 
            x = x//10
        return org == rev 