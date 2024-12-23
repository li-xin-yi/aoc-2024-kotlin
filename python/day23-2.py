import networkx as nx

with open('../inputs/day23.txt') as f:
    lines = f.readlines()

G = nx.Graph()
for line in lines:
    u, v = line.strip().split('-')
    G.add_edge(u, v)

clique, _ = nx.max_weight_clique(G, weight=None)

print(','.join(sorted(clique)))