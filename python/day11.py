from collections import Counter
import sys

input = sys.stdin.readline

inputs = list(map(int, input().strip().split()))

cnt = Counter(inputs)

T = 75

for _ in range(T):
    temp = Counter()
    for num in cnt:
        if num == 0:
            temp[1] += cnt[num]
        elif (n:=len(str(num)))%2 == 0:
            left, right = str(num)[:n//2], str(num)[n//2:]
            temp[int(left)] += cnt[num]
            temp[int(right)] += cnt[num]
        else:
            temp[num*2024] += cnt[num]
    cnt = temp

print(sum(cnt.values()))