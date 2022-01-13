# 1037 약수

n = int(input())
div = list(map(int, input().split()))
div.sort()
print(div[0] * div[-1])