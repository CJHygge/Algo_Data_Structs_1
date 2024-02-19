# Model the courses as a graph, where a prerequisite relation is held as a en edge
# N nodes, M prerequisites
# Edge prerequisite course -> current course
# Group courses in blocks (semesters)
# Topological order of the graph gives the order of the course blocks -> Course Plan
# 1. Build graph O(N+M) 
# 2. Find course with deg- = 0 O(N)
# 3. Take the course allowed before blocked courses and recurse further O(N+M)
# 4. Find last course, longest path in graph till end O(N)

import queue

# Take input
N,M = list(map(int,input().split()))
adj = [[] for _ in range(N)]
semester = [1 for _ in range(N)]
degIn = [0 for _ in range(N)]

# Build the graph
for _ in range(M):
    x, y = list(map(int,input().split()))
    # Append post course x to prereq y
    adj[y-1].append(x-1)
    # Increment the in degree of course x
    degIn[x-1] += 1

q = queue.Queue()

# Find course with in degree 0
for i in range(N):
    if (degIn[i]==0):
        # Select the first semester courses
        semester[i] = 1
        # Put into queue to be taken
        q.put(i)

# Take courses and recurse
while (not q.empty()):
    # Take a course
    r = q.get()
    for b in adj[r]:

        # Update prerequisite needs        
        degIn[b] -= 1
        if (degIn[b]==0):
            # If course available add to queue
            # to be taken in next semester
            semester[b] = semester[r]+1
            q.put(b)

# Latest semester - semester of the last course to be taken       
print(max(semester))
