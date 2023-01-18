# 2798 블랙잭

from itertools import combinations

def blackjack(array, M):
    result = []
    for data in list(combinations(array,3)):
        temp = sum(data)
        if temp == M:
            return M
        elif temp < M:
            result.append(temp)
    return max(result)
N,M = map(int,input().split())
array = list(map(int,input().split()))
print(blackjack(array,M))