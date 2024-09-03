class Solution(object):
    def chalkReplacer(self, chalk, k):
        total_chalk = sum(chalk)
        k %= total_chalk
        for i, pieces in enumerate(chalk):
            if k < pieces:
                return i
            k -= pieces