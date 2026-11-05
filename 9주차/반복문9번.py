n = int(input())

result = 1

for i in range(1, n + 1):
    result *= i
    if result > n:
        print(i)
        break
