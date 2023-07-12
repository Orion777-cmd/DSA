class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i, j = 0, 0
        s_dict = Counter()
        t_dict = Counter(t)

        res = []
        while j <= len(s)-1:
            s_dict[s[j]] += 1
            j += 1
            if s_dict & t_dict != t_dict:
                continue
            
            while i < j:
                s_dict[s[i]] -= 1
                i += 1
                if s_dict & t_dict == t_dict:
                    continue
                res.append(s[i-1:j])
                break
        return '' if not res else min(res, key=len)
