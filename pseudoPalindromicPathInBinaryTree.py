# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, count):
            if not node:
                return 0

            count[node.val] += 1

            if not node.left and not node.right:
                if self.canBePalindrome(count):
                    count[node.val] -= 1
                    return 1
                count[node.val] -= 1
                return 0

            left_count = dfs(node.left, count.copy())
            right_count = dfs(node.right, count.copy())

            count[node.val] -= 1

            return left_count + right_count

        return dfs(root, Counter())

    def canBePalindrome(self, count: Counter) -> bool:
        odd_count = 0
        for cnt in count.values():
            if cnt % 2 != 0:
                odd_count += 1
        return odd_count <= 1
