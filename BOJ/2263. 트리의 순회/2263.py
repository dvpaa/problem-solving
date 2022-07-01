import sys
sys.setrecursionlimit(10**9)


def find_pre_order(in_start, in_end, post_start, post_end):
    if in_start > in_end:
        return

    print(post_order[post_end], end=" ")
    idx = in_order_idx[post_order[post_end]]

    find_pre_order(in_start, idx - 1, post_start, post_start + idx - in_start - 1)
    find_pre_order(idx + 1, in_end, post_end - in_end + idx, post_end - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_order_idx = [0] * (n+1)
for i in range(n):
    in_order_idx[in_order[i]] = i
find_pre_order(0, n - 1, 0, n - 1)
