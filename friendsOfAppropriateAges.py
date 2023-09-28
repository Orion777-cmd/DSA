class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)
        single_age = [age for age in count.keys()]
        single_age.sort()
        prefix_sum = []
        for age in single_age:
            if not prefix_sum:
                prefix_sum.append(count[age])
            
            else:
                prefix_sum.append(count[age] + prefix_sum[-1])
        
        ans = 0
        
        for i in range(len(single_age)):
            age = single_age[i]

            start = 0
            end = i-1
            last = -1
            while start <= end:
                mid = (start + end)//2
                if single_age[mid] <= 0.5 * single_age[i] + 7:
                    start = mid + 1
                else:
                    last = mid
                    end = mid -1
            if last >= 0:
                if last == 0:
                    temp = prefix_sum[i-1]
                else:
                    temp = prefix_sum[i-1] - prefix_sum[last-1]
                ans += count[age] * temp
            
            if age > 14:
                ans += count[age] * (count[age] -1)
        return ans
        
