# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def flattenList(nested: NestedInteger) -> list[int]:
            result = []
            for each in nested:
                if each.isInteger():
                    result.append(each.getInteger())
                else:
                    result.extend(flattenList(each.getList()))
            return result
        self.flattened = flattenList(nestedList)
        self.index = 0    
    def next(self) -> int:
        num = self.flattened[self.index]
        self.index += 1
        return num
            
    def hasNext(self) -> bool:
        return True if self.index < len(self.flattened) else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())



####################### APPROACH TWO ============> USING STACK ############################################################


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.flattened = nestedList[::-1]
         
    def next(self) -> int:
        return self.flattened.pop().getInteger()
            
    def hasNext(self) -> bool:
        while self.flattened:
            top = self.flattened[-1]
            if top.isInteger():
                return True
            self.flattened = self.flattened[:-1] + top.getList()[::-1]
        return False
