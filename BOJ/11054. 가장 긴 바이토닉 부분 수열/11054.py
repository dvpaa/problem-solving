# 11054 가장 긴 바이토닉 부분 수열

n = int(input())
a = list(map(int, input().split()))
ar = a[::-1]
dp_a = [1] * n
dp_ar = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp_a[i] = max(dp_a[i], dp_a[j] + 1)
        if ar[i] > ar[j]:
            dp_ar[i] = max(dp_ar[i], dp_ar[j] + 1)
result = [0] * n
for i in range(n):
    result[i] = dp_a[i] + dp_ar[n-1-i] - 1
print(max(result))