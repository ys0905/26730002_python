max_num = 0

while True:
    n = int(input())

    if n == 0:
        break

    if n > max_num:
        max_num = n

print(max_num)
