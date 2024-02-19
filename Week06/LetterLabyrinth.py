from collections import deque


N = int(input())
labyr = [input() for i in range(N)]

def index(x,y):
    return x*N+y

def adjList():
    adj = [None]*(N**2)
    for i in range(N):
        for j in range(N):
            lis = []
            if i>0 and labyr[i-1][j] != labyr[i][j]:
                lis.append(index(i-1,j))
            if j<N-1 and labyr[i][j+1] != labyr[i][j]:
                lis.append(index(i,j+1))
            if i<N-1 and labyr[i+1][j] != labyr[i][j]:
                lis.append(index(i+1,j))
            if j>0 and labyr[i][j-1] != labyr[i][j]:
                lis.append(index(i,j-1))
            adj[index(i,j)] = lis
    return adj

adj = adjList()

def printAdjList(adj):
    for i in range(N**2):
        print("Node {} has adjacent nodes:{}".format(i,adj[i]))

#printAdjList(adj)

#Run breadth-first search from node x in graph
def BFS (x):
    q = deque()
    visited = [False for i in range(N**2)]
    distance = [-1 for i in range(N**2)]
    
    visited[x] = True
    distance[x] = 0
    q.append(x)
    while q:
        s = q.popleft()
        # process node s
        for u in adj[s]:
            if (visited[u]):
                continue
            visited[u] = True
            distance[u] = distance[s]+1
            q.append(u)
    return distance

#print(BFS(0))
print(BFS(0)[-1]+1)