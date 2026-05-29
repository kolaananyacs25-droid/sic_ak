t = int(input())

for _ in range(t):
    n = int(input())

    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))

    boys.sort()
    girls.sort()

    possible1 = True
    possible2 = True

    for i in range(n):
        if boys[i] > girls[i]:
            possible1 = False
            break

    for i in range(n - 1):
        if girls[i] > boys[i + 1]:
            possible1 = False
            break

    for i in range(n):
        if girls[i] > boys[i]:
            possible2 = False
            break

    for i in range(n - 1):
        if boys[i] > girls[i + 1]:
            possible2 = False
            break

    if possible1 or possible2:
        print("YES")
    else:
        print("NO")