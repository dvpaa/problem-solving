# 2447 별 찍기 - 10

def append_star(N):
    if N == 1:
        return ['*']
    stars = append_star(N // 3)
    L = []
    for star in stars:
        L.append(star * 3)
    for star in stars:
        L.append(star + ' ' * (N//3) + star)
    for star in stars:
        L.append(star * 3)
    return L

N = int(input())
print('\n'.join(append_star(N)))