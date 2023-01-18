# improved solution

def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < ((100 - p) // s):
            Q.append([((100 - p) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]
