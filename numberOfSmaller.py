len1, len2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = [0 for _ in range(len2)]

i = 0
j = 0
while j < len2:
    while i < len1 and arr1[i] < arr2[j]:
        i += 1
    res[j] = i
    j += 1
print(*res)
