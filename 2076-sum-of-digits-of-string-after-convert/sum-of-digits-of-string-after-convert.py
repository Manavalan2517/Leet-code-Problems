class Solution(object):
    def getLucky(self, s, k):
        lst = []
        for i in s:
            num = ord(i)-96
            if num > 9:
                for i in str(num):
                    lst.append(int(i))
            else: lst.append(num)
        res = sum(lst)
        while k > 1 and res > 9:
            res = sum(int(digit) for digit in str(res))
            k -= 1
        return res