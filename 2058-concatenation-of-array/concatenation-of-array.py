class Solution(object):
    def getConcatenation(self, nums):
        nums.extend(nums)
        return nums
        