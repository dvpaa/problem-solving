import sys


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b, parent_net):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        net = parent_net[a] + parent_net[b]
        if a < b:
            parent[b] = a
            parent_net[a] = net
        else:
            parent[a] = b
            parent_net[b] = net


for i in range(int(input())):
    F = int(input())
    friends = {}
    friend_net = {}

    for j in range(F):
        name1, name2 = sys.stdin.readline().rstrip().split()

        friends.setdefault(name1, name1)
        friends.setdefault(name2, name2)

        friend_net.setdefault(name1, 1)
        friend_net.setdefault(name2, 1)

        union_parent(friends, name1, name2, friend_net)
        print(friend_net[find_parent(friends, name1)])
