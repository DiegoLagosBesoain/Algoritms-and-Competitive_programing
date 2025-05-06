import sys
from collections import defaultdict, deque

def maxflow(grafo, s, t):
    G = defaultdict(list)
    edge_weights = defaultdict(int)

    for u in grafo:
        for v in grafo[u]:
            cap = grafo[u][v]
            G[u].append(v)
            G[v].append(u)
            edge_weights[(u, v)] += cap
            edge_weights[(v, u)] += 0

    def bfs():
        parent = {s: None}
        flow = {s: float('inf')}
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v in G[u]:
                if v not in parent and edge_weights[(u, v)] > 0:
                    parent[v] = u
                    flow[v] = min(flow[u], edge_weights[(u, v)])
                    if v == t:
                        return flow[t], parent
                    queue.append(v)
        return 0, parent

    total_flow = 0
    while True:
        new_flow, parent = bfs()
        if new_flow == 0:
            break
        total_flow += new_flow
        cur = t
        while cur != s:
            prev = parent[cur]
            edge_weights[(prev, cur)] -= new_flow
            edge_weights[(cur, prev)] += new_flow
            cur = prev

    return total_flow

T = int(sys.stdin.readline().strip())
for test_case in range(1, T + 1):
    n, m = map(int, sys.stdin.readline().strip().split())
    grafo = defaultdict(dict)

    
    bob_data = list(map(int, sys.stdin.readline().strip().split()))
    bob_stickers = bob_data[1:]
    bob_have = set(bob_stickers)

    bob_duplicates = defaultdict(int)
    for s in bob_stickers:
        bob_duplicates[s] += 1

    for sticker in range(1, m + 1):
        grafo[f"sticker{sticker}"] = {}

    
    grafo["S"] = {}
    grafo["T"] = {}

    
    for sticker in bob_duplicates:
        if bob_duplicates[sticker] > 1:
            grafo["S"][f"sticker{sticker}"] = bob_duplicates[sticker] - 1

    # Amigos
    for i in range(n - 1):
        friend_data = list(map(int, sys.stdin.readline().strip().split()))
        friend_stickers = friend_data[1:]
        count = defaultdict(int)
        for s in friend_stickers:
            count[s] += 1

        for s in range(1, m + 1):
            if count[s] == 0:
                grafo[f"sticker{s}"][f"friend{i}"] = 1  
            elif count[s] > 1:
                grafo[f"friend{i}"][f"sticker{s}"] = count[s] - 1  

   
    for sticker in range(1, m + 1):
        if sticker not in bob_have:
            grafo[f"sticker{sticker}"]["T"] = 1

    flow = maxflow(grafo, "S", "T")
    print(f"Case #{test_case}: {len(bob_have) + flow}")