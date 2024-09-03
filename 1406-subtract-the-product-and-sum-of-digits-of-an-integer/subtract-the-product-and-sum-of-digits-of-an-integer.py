class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        sum = 0
        while n>0:
            num = n%10
            sum += num
            product = product*num
            n //= 10
        result = product-sum
        return result