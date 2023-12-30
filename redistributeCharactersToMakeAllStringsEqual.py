class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)
        for word in words:
            for ch in word:
                count[ch] += 1
        
        for key, val in count.items():
            if val % len(words) != 0:
                return False
        return True
