# 1992 쿼드트리

import sys

N = int(sys.stdin.readline())
data = [sys.stdin.readline().rstrip() for _ in range(N)]
result = ''

def search_color(x, y, n):
    global result
    standard = data[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if data[i][j] != standard:
                result += '('
                search_color(x, y, n//2)
                result += ')'
                result += '('
                search_color(x, y+(n//2), n//2)
                result += ')'
                result += '('
                search_color(x+(n//2), y, n//2)
                result += ')'
                result += '('
                search_color(x+(n//2), y+(n//2), n//2)
                result += ')'
                return
    result += str(standard)
    return

search_color(0, 0, N)
result = result.replace(')(', '')
print(result)