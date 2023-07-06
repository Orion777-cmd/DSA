class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i, j = 0, len(skill)-1
        ans = 0
        goal = skill[i] + skill[j] 
        while i < j:
            if skill[i] + skill[j] != goal:
                ans = -1
                break
            
            ans += skill[i] * skill[j]
            i += 1
            j -= 1
        return ans
