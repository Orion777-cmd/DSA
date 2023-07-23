class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dirQueue = []
        radQueue = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                radQueue.append(i)
            else:
                dirQueue.append(i)
        n = len(senate)
        
        while dirQueue and radQueue:
            if dirQueue[0] < radQueue[0]:
                dirQueue.pop(0)
                radQueue.pop(0)
                dirQueue.append(n)
            else:
                dirQueue.pop(0)
                radQueue.pop(0)
                radQueue.append(n)
            n += 1
        
        return 'Radiant' if radQueue else 'Dire'

