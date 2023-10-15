class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i , j  = 0, 0
        res = 0
        count = {"T": 0, "F": 0}
        while j < len(answerKey):
            count[answerKey[j]] += 1
            while not (count['T'] <= k or count["F"] <=k):
                count[answerKey[i]] -= 1
                i+= 1
            j +=1
            res = max(res, j-i)
        return res
