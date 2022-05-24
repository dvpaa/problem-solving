def solution(priorities, location):
    arr = [(idx, val) for idx, val in enumerate(priorities)]
    cnt = 1
    while arr:
        idx, val = arr.pop(0)
        flag = True
        for tup in arr:
            if val < tup[1]:
                arr.append((idx, val))
                flag = False
                break

        if flag:
            if idx == location:
                return cnt
            else:
                cnt += 1
