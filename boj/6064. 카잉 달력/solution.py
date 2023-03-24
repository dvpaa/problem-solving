import sys
input = sys.stdin.readline

def find_gcd(a:int, b:int) -> int:
    if b == 0:
        return a
    return find_gcd(b, a%b)


def find_date(m: int, n: int, x: int, y: int) -> int:
    limit = m * (n // find_gcd(m, n))
    i = 0
    while True:
        result = i * m + x
        if result > limit:
            return -1

        if (result - y) % n == 0 and result >= y:
            return result

        i += 1

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(find_date(m, n, x, y))
