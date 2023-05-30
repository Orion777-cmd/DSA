class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        frequency = Counter(s)
        sorted_frequency = dict(sorted(frequency.items(), key=lambda item:item[1], reverse=True))
        for (key, value) in sorted_frequency.items():
            ans += key * value
        return ans
