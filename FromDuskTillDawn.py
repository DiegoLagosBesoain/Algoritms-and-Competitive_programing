import sys
import heapq, io
from collections import deque, defaultdict
import math
class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.capacity = defaultdict(dict)  # For flow problems
        self.cost = defaultdict(dict)      # For min-cost flow
        self.directed = directed

    def add_edge(self, u, v, weight=1, cap=None, cost=None):
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

        if cap is not None:
            self.capacity[u][v] = cap
            if not self.directed:
                self.capacity[v][u] = cap

        if cost is not None:
            self.cost[u][v] = cost
            if not self.directed:
                self.cost[v][u] = cost

    def update_edge(self, u, v, weight=None, cap=None, cost=None):
        # Update edge weight
        for i, (node, w) in enumerate(self.graph[u]):
            if node == v:
                if weight is not None:
                    self.graph[u][i] = (v, weight)
                break
        else:
            # Edge doesn't exist, add it
            self.graph[u].append((v, weight if weight is not None else 1))

        # Update capacity
        if cap is not None:
            self.capacity[u][v] = cap

        # Update cost
        if cost is not None:
            self.cost[u][v] = cost

        # For undirected graphs
        if not self.directed:
            self.update_edge(v, u, weight, cap, cost)

    def remove_edge(self, u, v):
        self.graph[u] = [(node, w) for node, w in self.graph[u] if node != v]
        self.capacity[u].pop(v, None)
        self.cost[u].pop(v, None)
        if not self.directed:
            self.remove_edge(v, u)

    def remove_node(self, u):
        self.graph.pop(u, None)
        self.capacity.pop(u, None)
        self.cost.pop(u, None)

        # Remove edges to u
        for v in list(self.graph):
            self.graph[v] = [(node, w) for node, w in self.graph[v] if node != u]
            self.capacity[v].pop(u, None)
            self.cost[v].pop(u, None)

    def has_node(self, u):
        return u in self.graph

    def has_edge(self, u, v):
        return any(node == v for node, _ in self.graph[u])


    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            u = queue.popleft()
            yield u
            for v, _ in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                yield u
                for v, _ in reversed(self.graph[u]):
                    stack.append(v)
    
    #returns the first path it finds with the lowest cost, regardless of the length
    def dijkstra(self, start):
        print(self.graph)
        dist = {}
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in self.graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return dist
    
    #same as the above, but this one returns the distance to one node, not to all
    def dijkstra_path(self, start, end):
        print(self.graph)
        dist = {}
        prev = {}
        heap = [(0, start)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            if u == end:
                break
            for v, w in self.graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
                    if v not in prev or d + w < dist.get(v, float('inf')):
                        prev[v] = u
        if end not in dist:
            return None, float('inf')
        path = []
        at = end
        while at != start:
            path.append(at)
            at = prev[at]
        path.append(start)
        path.reverse()
        return path, dist[end]


    def max_flow(self, s, t):
        parent = {}

        def bfs():
            visited = set()
            queue = deque([s])
            visited.add(s)
            parent.clear()

            while queue:
                u = queue.popleft()
                for v in self.capacity[u]:
                    if v not in visited and self.capacity[u][v] > 0:
                        visited.add(v)
                        parent[v] = u
                        if v == t:
                            return True
                        queue.append(v)
            return False

        flow = 0
        while bfs():
            path_flow = float('inf')
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u
            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v].setdefault(u, 0)
                self.capacity[v][u] += path_flow
                v = u
            flow += path_flow
        return flow

    def min_cost_flow(self, s, t, max_flow):
        n = defaultdict(lambda: float('inf'))
        flow = 0
        cost_total = 0

        def spfa():
            dist = defaultdict(lambda: float('inf'))
            in_queue = defaultdict(bool)
            parent = {}
            dist[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                in_queue[u] = False
                for v in self.capacity[u]:
                    if self.capacity[u][v] > 0:
                        new_dist = dist[u] + self.cost[u][v]
                        if new_dist < dist[v]:
                            dist[v] = new_dist
                            parent[v] = u
                            if not in_queue[v]:
                                q.append(v)
                                in_queue[v] = True
            return dist, parent

        while flow < max_flow:
            dist, parent = spfa()
            if t not in parent:
                break
            # Find bottleneck
            path_flow = max_flow - flow
            v = t
            while v != s:
                u = parent[v]
                path_flow = min(path_flow, self.capacity[u][v])
                v = u
            # Update capacities
            v = t
            while v != s:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                self.capacity[v].setdefault(u, 0)
                self.capacity[v][u] += path_flow
                cost_total += path_flow * self.cost[u][v]
                v = u
            flow += path_flow
        return flow, cost_total
    
    #returns every path from a to b with their associated cost, in the format [[[path],cost],[[path],cost]]
    def all_paths_with_cost(self, start, end):
        def dfs(u, path, cost, visited):
            if u == end:
                result.append((list(path), cost))
                return
            for v, w in self.graph[u]:
                if v not in visited:
                    visited.add(v)
                    path.append(v)
                    dfs(v, path, cost + w, visited)
                    path.pop()
                    visited.remove(v)

        result = []
        visited = set([start])
        dfs(start, [start], 0, visited)
        return result
    

    def bipartite(self, start, color, colors):
        """
        Check if the connected component starting from `start` is bipartite.
        Uses BFS to attempt a 2-coloring of the graph.
        
        Args:
            start: The starting node for the component.
            color: The initial color to assign to the starting node (0 or 1).
            colors: A dictionary mapping nodes to their color (-1 if unvisited).

        Returns:
            The size of the larger color class if the component is bipartite,
            otherwise 0 if the component contains an odd cycle.
        """
        queue = deque([start])
        colors[start] = color
        count = [0, 0]
        count[color] += 1
        component_nodes = [start]
        is_valid = True

        while queue:
            u = queue.popleft()
            for v, _ in self.graph[u]:  # Use self.graph to access adjacency list
                if colors[v] == -1:
                    colors[v] = 1 - colors[u]
                    count[colors[v]] += 1
                    queue.append(v)
                    component_nodes.append(v)
                elif colors[v] == colors[u]:
                    is_valid = False

        for node in component_nodes:
            colors[node] = 2  # Mark as processed

        return max(count) if is_valid else 0
def es_noche(h):
    return h >= 18 or h <= 6

T=int(sys.stdin.readline().strip())
for caso in range(T):
    c=int(sys.stdin.readline().strip())
    grafo=Graph(directed=True)
    rutas_aceptadas=[]
    for ruta in range(c):
        inicio,fin,hora_inicio,duracion=sys.stdin.readline().strip().split()
        hora_llegada=(int(hora_inicio)+int(duracion))%24
        if int(duracion) <= 12 and es_noche(int(hora_inicio)) and es_noche(hora_llegada):
            if (int(hora_inicio)+int(duracion))>24:
                grafo.add_edge(inicio, fin)
            else:
                print("entre")
                grafo.add_edge(inicio, fin,0)
    S,D=sys.stdin.readline().strip().split()
    print(grafo)
    print(grafo.dijkstra_path(S,D))
        

