class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        odd_count = 0
        for char in set(s):
            if s.count(char) % 2 != 0:
                odd_count += 1
        return k >= odd_count