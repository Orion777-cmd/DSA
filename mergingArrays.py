len1, len2 = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
sorted = []
i = j = 0
while i < len1 and j < len2:
    if arr1[i] < arr2[j]:
        sorted.append(arr1[i])
        i += 1
    else:
        sorted.append(arr2[j])
        j += 1
if i < len1:
    sorted.extend(arr1[i:])
elif j < len2:
    sorted.extend(arr2[j:])
print(*sorted)
