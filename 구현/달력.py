import sys

n = int(sys.stdin.readline())
cal = [0] * 366
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    for i in range(start, end + 1):
        cal[i] += 1

row = 0
col = 0
result = 0
for day in cal:
    if day != 0:
        col = max(col, day)
        row += 1
    else:
        result += row * col
        row = 0
        col = 0
result += row * col
print(result)