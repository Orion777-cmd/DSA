class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = ''
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            if ord(word1[i]) > ord(word2[j]):
                merge += word1[i]
                i += 1
            elif word2[j] > word1[i]: 
                merge += word2[j]
                j += 1
            else:
                if word1[i:] > word2[j:]:
                    merge += word1[i]
                    i += 1
                else:
                    merge += word2[j]
                    j += 1
        if i < len(word1):
            merge += word1[i:]
        if j < len(word2):
            merge += word2[j:]
        return merge
