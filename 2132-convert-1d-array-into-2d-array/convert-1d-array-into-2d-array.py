class Solution(object):
    def construct2DArray(self, original, m, n):
        lst = []
        if len(original) == m*n:
            for i in range(0,m*n,n):
                lst.append(original[i:i+n])
            return lst
        return []