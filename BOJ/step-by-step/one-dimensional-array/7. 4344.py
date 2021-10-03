# 4344 평균은 넘겠지

C = int(input())
for _ in range(C):
    array = list(map(int, input().split()))
    avg = sum(array[1:])/array[0]
    print("{:.3f}%".format(len([x for x in array[1:] if x > avg]) / array[0] * 100))