class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        array = [0] * 60
        res = 0
        for i in range(len(time)):
            
            complement = (60 - time[i] % 60) % 60
            res += array[complement]
            array[time[i] % 60] += 1
        return res
        
