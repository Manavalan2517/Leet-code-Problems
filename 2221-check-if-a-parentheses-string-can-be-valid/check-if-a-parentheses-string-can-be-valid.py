class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open = 0
        balance = 0
        for i in range(len(s)):
            if locked[i] == '0':
                open += 1
            elif s[i] == '(':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                if open > 0:
                    open -= 1
                    balance += 1
                else:
                    return False

        close = 0
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '0':
                close += 1
            elif s[i] == ')':
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                if close > 0:
                    close -= 1
                    balance += 1
                else:
                    return False

        return True