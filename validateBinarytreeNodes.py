class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        def findRoot() -> int:

            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        
        root = findRoot()
        if root == -1: return False

        visited = {root}
        stack = [root]
        while stack:
            temp = stack.pop()
         
            for child in [leftChild[temp], rightChild[temp]]:
                if child != -1:
                    if child in visited:
                        return False
                    
                    stack.append(child)
                    visited.add(child)
        return len(visited) == n

        
