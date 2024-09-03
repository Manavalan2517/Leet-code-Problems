class Solution(object):
    def numberOfSteps(self, num):
        count = -1
        while num > 0:
            if num%2==0: 
                num//=2
                count += 1
            else: 
                num -= 1
                count += 1
                if num%2==0:
                    num//=2
                    count += 1
        if count < 0: return 0
        return count