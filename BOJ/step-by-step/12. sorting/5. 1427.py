# 1427 소트인사이드

N = input()
L = list(map(int, N))
L.sort(reverse = True)
print(''.join(map(str, L)))