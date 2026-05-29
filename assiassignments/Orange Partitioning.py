n = int(input())
orange = list(map(int, input().split()))

pivot = orange[n - 1]
k = 0

for i in range(n - 1):
    if orange[i] <= pivot:
        orange[k], orange[i] = orange[i], orange[k]
        k += 1

orange[k], orange[n - 1] = orange[n - 1], orange[k]

print(*orange)