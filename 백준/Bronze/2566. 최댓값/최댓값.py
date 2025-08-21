import sys

input = sys.stdin.readline

ans = -1
for i in range(9):
    row = list(map(int, input().split()))
    max_num = max(row)
    if ans < max_num:
        ans = max_num
        x = i + 1
        y = row.index(max_num) + 1

print(ans)
print(x, y)