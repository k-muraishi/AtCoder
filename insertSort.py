
n = int(input()) #一行目
A = list(map(int, input().split())) #2行目

for i in range(1, n):
    print(' '.join(map(str, A)))
    temp = A[i]
    j = i -1
    while A[j] > temp and j >= 0:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = temp
    
print(' '.join(map(str, A)))