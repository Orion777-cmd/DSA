class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        paths = [_ for _ in path if _] 
        for i in paths:
            if (not stack and i == '..') or i == '.':
                continue
            elif stack and i =='..':
                stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)

        
