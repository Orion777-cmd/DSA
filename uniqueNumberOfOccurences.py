class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        val = set(count.values())
        return len(count.keys()) == len(val)
