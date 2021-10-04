# 1542 평균

N = int(input())
score = list(map(int, input().split()))
maxscore = max(score)
new = 0

for s in score:
    new += s / maxscore * 100

print(new/N)