import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
nums = list(map(int, input().strip()))
n = len(nums)
gaps = defaultdict(list)
blocks = []
cur = 0
for i, num in enumerate(nums):
    if i % 2 == 1:
        if num != 0:
            gaps[num].append(cur)
    else:
        blocks.append((cur, num, i//2))
    cur += num

for gap in gaps:
    heapq.heapify(gaps[gap])

def find_first_index(start, length):
    idx, t = start, length
    for k in range(length, 10):
        if gaps[k] and gaps[k][0] < idx:
            idx, t = gaps[k][0], k
    if idx == start:
        return start
    else:
        heapq.heappop(gaps[t])
        if t > length:
            heapq.heappush(gaps[t-length], idx + length)
        return idx





res = 0
for cur, num, i in blocks[::-1]:
    idx = find_first_index(cur, num)
    res += i * ((2*idx + num - 1) * num // 2)


print(res)