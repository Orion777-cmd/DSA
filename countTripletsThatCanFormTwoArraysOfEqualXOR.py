class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        triplets = []
        prefix = [0]
        for i in range(len(arr)):
            prefix.append(arr[i]^prefix[-1])
       
        for j in range(1,len(arr)):
            for i in range(0, j):
                xors_i = prefix[j] ^ prefix[i]
                for k in range(j, len(arr)):
                    xors_k = prefix[k+1] ^ prefix[j]
                    if xors_i == xors_k:
                        triplets.append((i, j, k))
        return len(triplets)
