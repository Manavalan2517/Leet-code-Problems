class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if (words[i] in words[j]) and (words[i] != words[j]):
                    if words[i] in result:
                        continue
                    result.append(words[i])
        return result