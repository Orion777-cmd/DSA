class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_length = len(words) * word_length
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            curr_count = Counter()
            j = 0

            while j < total_length:
                word = s[i+j:i+j+word_length]
                if word not in word_count or curr_count[word] >= word_count[word]:
                    break
                curr_count[word] += 1
                j += word_length

            if j == total_length:
                result.append(i)

        return result
