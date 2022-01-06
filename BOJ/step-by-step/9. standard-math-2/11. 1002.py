# 1002 터렛

T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    R = [r1,r2,d]
    m = max(R); R.remove(m)
    print(-1 if (d==0 and r1==r2) else 1 if (m == sum(R)) else 0 if (m > sum(R)) else 2)