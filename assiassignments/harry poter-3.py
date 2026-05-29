n = int(input())

coins = list(map(int, input().split()))

q, x = map(int, input().split())

stack = []
total = 0
idx = 0

answer = -1

for _ in range(q):
    operation = input().strip()

    if operation == "Harry":
        stack.append(coins[idx])
        total += coins[idx]
        idx += 1

    else:  # Remove
        if stack:
            total -= stack.pop()

    if total == x:
        answer = len(stack)
        break

print(answer)