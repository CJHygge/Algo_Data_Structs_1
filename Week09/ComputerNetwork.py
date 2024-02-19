from gettext import find
from re import I


class Quick:

    def __init__(self, N):
        self.p = [0] * N
        self.sz = [1] * N
        for k in range(N):
            self.p[k] = k

    def find(self,i):
        while (i != self.p[i]):
            i = self.p[i]
        return i

    def findPathCom(self,i):
        if (i != self.p[i]):
            self.p[i] = self.findPathCom(self.p[i])
        return self.p[i]

    def union(self,i,j):
        ri = self.find(i)
        rj = self.find(j)
        if (ri != rj):
            if (self.sz[ri] <= self.sz[rj]):
                self.p[ri] = rj
                self.sz[rj] += self.sz[ri]
            else:
                self.p[rj] = ri
                self.sz[ri] += self.sz[rj]

#reader = iter(open('test.txt').read().split('\n'))
#input = lambda: next(reader)

N,M = map(int,input().split(' '))
lines = [input() for _ in range(M)]
quick = Quick(N)

for line in lines:
    args =  line.split(' ')
    if args[0]=='A':
        quick.union(int(args[1]),int(args[2]))
    elif args[0]=='C':
        print("YES") if quick.findPathCom(int(args[1]))==quick.findPathCom(int(args[2])) else print("NO")

