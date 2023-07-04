class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subs = ""
                while stack[-1] != "[":
                    subs = stack.pop() + subs
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop()+k
                stack.append(int(k) * subs)
        return "".join(stack)
                
        
