import heapq


def solution(scoville, K):
    q = []
    for s in scoville:
        heapq.heappush(q, s)

    cnt = 0

    while True:
        first = heapq.heappop(q)
        if first >= K:
            break
        if not q:
            return -1
        sec = heapq.heappop(q)
        heapq.heappush(q, first + (sec * 2))
        cnt += 1

    return cnt
