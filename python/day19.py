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
    seen = set([0])
    def dfs(i):
        root = trie
        for j in range(i, len(s)):
            if s[j] not in root:
                return
            if '#' in root[s[j]]:
                seen.add(j+1)
            root = root[s[j]]

    for i in range(len(s)):
        if i in seen:
            dfs(i)
    return len(s) in seen

print(len([s for s in lst if check(s)]))
