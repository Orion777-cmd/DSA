class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        key =len(count.keys())
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
                count[i] -= 1
           
            elif stack and i not in stack and ord(stack[len(stack)-1]) > ord(i) and stack[len(stack)-1] in count.keys():
                while stack and stack[len(stack)-1] in count.keys() and ord(stack[len(stack)-1]) >ord(i) :
                    stack.pop()
                if i not in stack:
                    stack.append(i)
                    count[i]-= 1
            elif stack and i not in stack:
                stack.append(i)
                count[i] -= 1
            else:
                count[i]-= 1
            if count[i]==0:
                del count[i]
            
            
        return "".join(stack)
