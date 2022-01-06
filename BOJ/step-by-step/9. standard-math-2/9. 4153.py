# 4153 직각삼각형

while True:
    tri = list(map(int,input().split()))
    if tri == [0,0,0]:
        break
    c = max(tri)
    tri.remove(c)
    if c*c == (tri[0]*tri[0] + tri[1]*tri[1]):
        print("right")
    else:
        print("wrong")