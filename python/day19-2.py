from collections import Counter
with open('../inputs/day19.txt') as f:
    lines = f.readlines()

patterns = lines[0].strip().split(', ')
lst = [line.strip() for line in lines[2:]]

trie = {}
for pattern in patterns:
    root = trie
    for c in pattern:
        if c not in root:
            root[c] = {}
        root = root[c]
    root['#'] = {}

def check(s):
    cnt = Counter({0:1})
    def dfs(i):
        root = trie
        for j in range(i, len(s)):
            if s[j] not in root:
                return
            if '#' in root[s[j]]:
                cnt[j+1] += cnt[i]
            root = root[s[j]]

    for i in range(len(s)):
        if i in cnt:
            dfs(i)
    return cnt[len(s)]

print(sum([check(s) for s in lst]))
