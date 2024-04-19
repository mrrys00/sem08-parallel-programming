from collections import defaultdict, deque
import heapq
import random

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight=0):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def dfs(self, start):
        visited = set()
        stack = [start]
        result = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                stack.extend(neighbor for neighbor, _ in reversed(self.graph[node]) if neighbor not in visited)

        return result

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(neighbor for neighbor, _ in self.graph[node] if neighbor not in visited)

        return result

    def kruskal_mst(self):
        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        edges = [(weight, u, v) for u, neighbors in self.graph.items() for v, weight in neighbors]
        edges.sort()

        parent = {node: node for node in self.graph}
        rank = {node: 0 for node in self.graph}
        mst = []

        for weight, u, v in edges:
            if find(parent, u) != find(parent, v):
                mst.append((u, v, weight))
                union(parent, rank, u, v)

        return mst

def generate_random_graph(num_nodes, num_edges):
    graph = Graph()
    for _ in range(num_edges):
        u = random.randint(1, num_nodes)
        v = random.randint(1, num_nodes)
        weight = random.randint(1, 100)
        graph.add_edge(u, v, weight)
    return graph

# Example usage:
num_nodes = 10**5
num_edges = 20**5
graph = generate_random_graph(num_nodes, num_edges)

print("DFS:", graph.dfs(1))
print("BFS:", graph.bfs(1))
print("Minimum Spanning Tree (Kruskal):", graph.kruskal_mst())
