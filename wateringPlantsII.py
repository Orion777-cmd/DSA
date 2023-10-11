class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        refill = 0
        left , right = 0 , len(plants)-1 
        a, b = capacityA, capacityB
        while left <= right:
            if left == right:
                if capacityA >= capacityB:
                    if capacityA - plants[left] <0:
                        refill += 1
                    left += 1
                else:
                    if capacityB - plants[right] <0:
                        refill += 1
                    right -= 1

            elif capacityA -plants[left] >= 0 and  capacityB - plants[right] >=0:
                capacityA -= plants[left]
                capacityB -= plants[right]
                left += 1
                right -= 1
            elif capacityA -plants[left] < 0 and   capacityB - plants[right] >=0:
                refill += 1
                capacityA = a
            elif   capacityB - plants[right] < 0 and  capacityA -plants[left] >= 0:
                refill += 1
                capacityB = b
            else:
                refill += 2
                capacityA, capacityB = a, b

        return refill
        
