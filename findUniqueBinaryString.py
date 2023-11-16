class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
       
        leng = len(nums[0])
        nums = set(nums)
        def backtracking(string):
            
            if len(string) == leng:
                if string not in nums:
                    return string
                return ""
                        
            result = backtracking(string + "1")
            if result: return result
            result = backtracking(string+"0")

            return result
        
        return backtracking("")
