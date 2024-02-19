multiple_numbers = list(map(int, input().split())) # Multiple integers on a line
A = multiple_numbers[0]
L = multiple_numbers[1]
O = multiple_numbers[2]
if ((A < L) & (A < O)):
    print("Anna")
        
if (L < A):
    print("Laura")

if ((O < A) or (O < L)): 
    print("Oscar")
       

if ((A == L) & (L <= O) | ((A == O) & (A == L))):
    print("NONE")