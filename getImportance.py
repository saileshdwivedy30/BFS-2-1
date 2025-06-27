# Time Complexity : O(n), where n is the number of employees
# Space Complexity : O(n), for the hashmap and recursion stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# I used a hashmap for quick access to employees by ID and performed DFS to sum up their importance

# Definition for Employee.
# class Employee:
#     def __init__(self, id: int, importance: int, subordinates: List[int]):
#         self.id = id
#         self.importance = importance
#         self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {emp.id: emp for emp in employees}

        def dfs(emp_id):
            emp = emp_map[emp_id]
            total = emp.importance
            for sub_id in emp.subordinates:
                total += dfs(sub_id)
            return total

        return dfs(id)
