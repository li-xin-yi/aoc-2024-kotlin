with open('../inputs/day02.txt') as f:
    lines = f.readlines()


res = 0
for line in lines:
    lst = list(map(int, line.strip().split()))
    # print(lst)
    diff = [b-a for a, b in zip(lst, lst[1:])]
    # print(diff) 
    if any(d * diff[0] <= 0 for d in diff[1:]):
        continue
    res += int(all(abs(d) <=3 for d in diff))

print(res)