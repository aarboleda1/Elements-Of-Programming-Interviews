"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node
in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j
for which the edge between nodes i and j exists.  Each node is an integer
between 0 and graph.length - 1.  There are no self edges or parallel edges:
graph[i] does not contain i, and it doesn't contain any element twice.

Basic Idea: Each vertice in the graph must be in 2 different sets.

Traverse the graph using BFS or DFS. For each vertice, we need to check
it's neighbors and keep the variant that the current vertice and its neighbors
are not in the same set.

If it hasn't yet been visited, use coloring and mark it in an auxilary data
structure. For this problem, we can use an array and its indices, since there
are 0 to n - 1 vertices

If it has been visited, and the colors are the same, it means they are in the
same set, which does not satisfy the property of a bi-partite graph

[ATTEMPTED] - 5/20
"""

UNSEEN = 0
RED = 1
BLUE = -1
# BFS
def isBipartite(self, graph: List[List[int]]) -> bool:
    q = deque([])
    coloring = [0] * len(graph)

    for i in range(len(graph)):
        # important, if it's already been seen, then skip
        if coloring[i] != UNSEEN:
            continue
        q.append(i)
        coloring[i] = RED

        while q:
            cur_vertice = q.popleft()
            for nei in graph[cur_vertice]: # neighbors
                if coloring[nei] == 0:
                    coloring[nei] = -coloring[cur_vertice]
                    q.append(nei)
                elif coloring[nei] != -coloring[cur_vertice]:
                    return False
    return True

# DFS
def isBipartite(self, graph: List[List[int]]) -> bool:
    coloring = [0] * len(graph)
    def dfs(cur):
        for nei in graph[cur]:
            if coloring[nei] == UNSEEN:
                # If it hasn't been seen, then mark it as the opposite
                # of the CURRENT VALUE,
                coloring[nei] = -coloring[cur]
                if not dfs(nei):
                    return False
            elif coloring[nei] != -coloring[cur]:
                return False
        return True

    for i in range(len(graph)):
        if coloring[i] == UNSEEN:
            coloring[i] = RED
        if not dfs(i):
            return False
    return True
