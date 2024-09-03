class Solution(object):
    def maximumWealth(self, accounts):
        maxx = 0
        for i in accounts:
            res = sum(i)
            if res > maxx: maxx = res
        return maxx