class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2_count = [0] * 26
        for word in words2:
            temp_count = [0] * 26
            for char in word:
                temp_count[ord(char) - ord('a')] += 1
            for i in range(26):
                words2_count[i] = max(words2_count[i], temp_count[i])
        result = []
        for word in words1:
            word_count = [0] * 26
            for char in word:
                word_count[ord(char) - ord('a')] += 1
            is_universal = True
            for i in range(26):
                if word_count[i] < words2_count[i]:
                    is_universal = False
                    break
            if is_universal:
                result.append(word)

        return result