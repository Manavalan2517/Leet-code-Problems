class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverse = 0
        temp = x
        while temp > 0:
            reverse = (reverse * 10) + (temp % 10)
            temp //= 10
        return x == reverse