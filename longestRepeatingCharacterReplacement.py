class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict = {}
        res = 0
        l = 0
        for i in range(len(s)):
            dict[s[i]]  = 1 + dict.get(s[i], 0)
            if (i-l+1) - max(dict.values()) > k:
                dict[s[l]] -= 1
                l+= 1
            res = max(res, i-l+1)
        return res
