class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sta1, sta2 = [],[]
        
        for i in s:
            if i =="#" and sta1:
                sta1.pop(0)
            elif i != "#":
                sta1.insert(0, i)
        for j in t:
            if j =="#" and sta2:
                sta2.pop(0)
            elif j != "#":
                sta2.insert(0, j)
        if sta1 == sta2:
            return True
        else:
            return False
        
