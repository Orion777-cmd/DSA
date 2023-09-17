"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        total_importance = 0
        emp_dict = {em.id: em for em in employees}

        def dfs(emp_id):
            nonlocal total_importance
            employ = emp_dict[emp_id]
            total_importance += employ.importance

            for sub_ids in employ.subordinates:
                dfs(sub_ids)
            
            return total_importance
        return dfs(id)
