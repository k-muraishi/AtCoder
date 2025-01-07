n = int(input())
A = [int(input()) for _ in range(n)]

unique = []
for i in range(len(A)):
    if A[i] not in unique:
        unique.append(A[i]) 
    
print(len(unique))