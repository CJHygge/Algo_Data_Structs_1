N = int(input())
A = list(map(int, input().split())) # Multiple integers on a line

def FINDMAX(A, n):
    max = 0
    for i in range(0, n):
         if (A[i] > A[max]):
             max = i
    return max

print(FINDMAX(A, N))