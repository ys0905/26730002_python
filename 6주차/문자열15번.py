hour, minute = map(int, input().split())

if hour >= 12:
    time = "PM"
else:
    time = "AM"

if hour >= 13:
    hour = hour - 12

print(f"{hour:02d} : {minute:02d} {time}")
