# use dictionary to represent a graph
from collections import defaultdict

# Initialize graph
adj_list = defaultdict(list)

# Add edge
def add_edge(u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)  # for undirected

# Example
add_edge(0, 1)
add_edge(1, 2)

# Traversing neighbors of node 1
for neighbor in adj_list[1]:
    print(neighbor)

# For weighted graph we can use a tuple
adj_list[u].append((v, weight))
adj_list[v].append((u, weight))  # if undirected

