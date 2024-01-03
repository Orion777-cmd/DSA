class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        j = 0
        laser = 0
        prevOne = bank[j].count("1")
        for i in range(1, len(bank)):
            curOne = bank[i].count("1")
            if prevOne > 0 and curOne > 0:
                laser += prevOne * curOne
                j += 1
                prevOne = curOne
            elif curOne == 0:
                continue
            elif prevOne == 0:
                prevOne = curOne
        return laser
