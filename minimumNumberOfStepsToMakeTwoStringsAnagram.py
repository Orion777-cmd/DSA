class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        tCount = Counter(t)
        op = 0
        for key in t:
            if key not in sCount:
                op += 1
            elif tCount[key] > sCount[key]:
                op += tCount[key] - sCount[key]
                sCount[key] += tCount[key]-sCount[key]
                
        return op
