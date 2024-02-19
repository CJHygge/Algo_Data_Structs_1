import sys
sys.setrecursionlimit(5000)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def treeDepth(root):
    if root is None:
        return 0
    else:
        return 1 + max(treeDepth(root.left), treeDepth(root.right))

N = int(input())

binTree = [0]*N
binTree[0] = Node(int(input()))

for i in range(1,N):
    line = input().split()
    binTree[i] = Node(int(line[2]))
    if (line[1]=='L'):
        binTree[int(line[0])].left = binTree[i]
    else:
        binTree[int(line[0])].right = binTree[i]

print(treeDepth(binTree[0])-1)