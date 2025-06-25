# Use matrix
# Initialize graph with n nodes
n = 5
adj_matrix = [[0] * n for _ in range(n)]

# Add an edge from u to v
def add_edge(u, v):
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1  # for undirected

# Example
add_edge(0, 1)
add_edge(1, 2)

# for weighted graph
adj_matrix[u][v] = weight
adj_matrix[v][u] = weight  # if undirected
