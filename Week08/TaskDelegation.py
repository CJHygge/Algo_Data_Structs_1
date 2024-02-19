class Node:
    def __init__(self, dif, id):
        self.key = dif
        self.id = id
    
class Heap:
    def __init__(self):
        self.array = [None]
        self.size = 0
    
    def less(self, x, y):
        return 1<=x<=self.size and 1<=y<=self.size and self.array[x].key < self.array[y].key
    
    def swap(self, parent, child):
        temp = self.array[parent]
        self.array[parent] = self.array[child]
        self.array[child] = temp

    def bubbleDown(self, node):
        left = node*2
        child = left + self.less(left, left+1)
        if self.less(node, child):
            self.swap(node, child)
            self.bubbleDown(child)

    def bubbleUp(self, node):
        parent = node//2
        if self.less(parent, node):
            self.swap(parent, node)
            self.bubbleUp(parent)


    def insert(self, node):
        self.array.append(node)
        self.size += 1
        self.bubbleUp(self.size)


    def extractMax(self):
        node = self.array[1]
        self.array[1] = self.array[self.size]
        self.array.pop()
        self.size -= 1
        self.bubbleDown(1)
        return node

#reader = iter(open('test.txt').read().split('\n'))
#input = lambda: next(reader)

heap = Heap()
N = int(input())

lines = [input().split(' ') for i in range(N)]
for line in lines:
    if len(line) == 3:
        heap.insert(Node(int(line[2]),int(line[1])))
    else:
        node = heap.extractMax()
        print(node.id)
