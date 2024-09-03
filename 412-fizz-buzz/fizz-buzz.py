class Solution(object):
    def fizzBuzz(self, n):
        lst = []
        for i in range(1, n+1):
            if (i%3==0) and (i%5==0): 
                lst.append("FizzBuzz") 
                continue
            if (i%3==0): 
                lst.append("Fizz")
                continue
            if (i%5==0): 
                lst.append("Buzz")
                continue
            else: lst.append(str(i))
        return lst