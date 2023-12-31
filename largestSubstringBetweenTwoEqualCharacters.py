class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = defaultdict(list)
        for i in range(len(s)):
            count[s[i]].append(i)
        res = -1
        for val in count.values():
            max_ = max(val)
            min_ = min(val)
            res = max(res, max_- min_-1)
        return res
