class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0 or x> 2**31 - 1:
            return False
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False
        
        
        
        num = 0
        a = abs(x)
        
        while (a!=0):
            temp = a % 10
            num = num *10 + temp
            a = int(a / 10)
        if x >=0 and x == num:
            return True
        else:
            return False