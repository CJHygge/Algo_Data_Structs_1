from heapq import heappush, heappop

N,M = map(int, input().split())

def AdjList():
    adj = [[] for _ in range(N)]
    for _ in range(M):
        i, j, w = map(int, input().split())
        (adj[i-1]).append((w, j-1))
        (adj[j-1]).append((w, i-1))
    return adj

def printAdjList(adj):
    for i in range(N):
        print("Building {} has adjacent buildings {}".format(i,adj[i]))

G = AdjList()
#printAdjList(G)

def Prim(G, s):
    heap = []
    visited = [False for _ in range(N)]
    total_price = 0

    heappush(heap, (0, s))
    
    while (heap):
        p, u = heappop(heap)
        if (not visited[u]):
            visited[u] = True
            total_price += p

            for p2, v in G[u]:
                if (not visited[v]):
                    heappush(heap, (p2,v))
    return total_price
    
print(Prim(G,0))