# 2775 부녀회장이 될테야

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    A = list(range(1, n+1))
    for i in range(k):
        for j in range(2,n+1):
            A[j-1] = A[j-2]+A[j-1]
    print(A[-1])