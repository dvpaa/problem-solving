# 2004 조합 0의 개수

def two_cnt(N):
    cnt = 0
    while N >= 2:
        cnt += N//2
        N //= 2
    return cnt
def five_cnt(N):
    cnt = 0
    while N >= 5:
        cnt += N//5
        N //= 5
    return cnt

n, m = map(int, input().split())
print(min(two_cnt(n) - (two_cnt(m)+two_cnt(n-m)), five_cnt(n) - (five_cnt(m)+five_cnt(n-m))))