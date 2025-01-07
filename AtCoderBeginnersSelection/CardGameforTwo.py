n = int(input())
a = list(map(int, input().split()))

alice = []
bob = []
asum = 0
bsum = 0

flg = True

def getMaxIndex(a):
    index = 0
    for i in range(len(a)):
        if a[index] < a[i]:
            index = i
    return index

while flg :
    if len(a) != 0:
        index = getMaxIndex(a)
        alice.append(a.pop(index))
    else:
        flg = False
        break

    if len(a) != 0:
        index = getMaxIndex(a)
        bob.append(a.pop(index))
    else:
        flg = False

for i in range(len(alice)):
    asum += alice[i]

for i in range(len(bob)):
    bsum += bob[i]

ans = asum - bsum

print(ans)    
