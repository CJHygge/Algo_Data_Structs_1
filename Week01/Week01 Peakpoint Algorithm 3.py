import math

# N = int(input())
# A = list(map(int, input().split()))  # Multiple integers on a line
N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def peak3(a, i, j):
    m = (math.floor((i + j)/2))
    if (a[m] >= a[m - 1]) & (a[m] >= a[m + 1]):
        return m
    elif a[m - 1] > a[m]:
        return peak3(a, i, m - 1)
    elif a[m] < a[m + 1]:
        return peak3(a, m + 1, j)


print(peak3(A, 0, N-1))


4
then 5 to 9
7
then 8 to 9
8
then 9 to 9
