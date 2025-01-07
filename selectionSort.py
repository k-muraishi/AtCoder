n = int(input())
A = list(map(int, input().split()))
cnt = 0

for i in range(n):
    minj = i
    for j in range(i, n):
        if A[j] < A[minj]:
            minj = j
    A[i], A[minj] = A[minj], A[i]
    if minj != i:
        cnt += 1
print(' '.join(map(str, A)))
print(cnt)