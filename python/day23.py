import networkx as nx

with open('../inputs/day23.txt') as f:
    lines = f.readlines()

G = nx.Graph()
for line in lines:
    u, v = line.strip().split('-')
    G.add_edge(u, v)

cycles = list(nx.simple_cycles(G, length_bound=3))

res = 0
for cycle in cycles:
    if len(cycle) != 3:
        continue
    for node in cycle:
        if node.startswith('t'):
            res += 1
            break

print(res)