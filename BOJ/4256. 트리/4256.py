def find_post_order(pre_order: list, in_order: list):
    if not in_order:
        return

    p = pre_order.pop(0)
    idx = in_order.index(p)

    find_post_order(pre_order, in_order[:idx])
    find_post_order(pre_order, in_order[idx + 1:])
    print(p, end=" ")


for _ in range(int(input())):
    n = int(input())
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    find_post_order(pre_order=pre_order, in_order=in_order)
    print()
