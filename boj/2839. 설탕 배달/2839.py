# 2839 설탕 배달

N = int(input())
cnt = 0
while N >= 3:
    if N % 5 == 0:
        cnt += N // 5
        N = 0
        break
    else:
        N -= 3
        cnt += 1
print(-1) if N != 0 else print(cnt)