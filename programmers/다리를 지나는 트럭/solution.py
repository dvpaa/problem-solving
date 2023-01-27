from collections import deque

def solution(bridge_length, weight, truck_weights):
    present_trucks = deque([(truck_weights[0], 0)])
    trucks = deque(truck_weights[1:])

    cnt = 1
    while present_trucks:
        if cnt - present_trucks[0][1] == bridge_length:
            present_trucks.popleft()

        push(bridge_length, weight, trucks, present_trucks, cnt)
        cnt += 1

    return cnt


def push(bridge_length, weight, trucks, present_trucks, cnt):
    if not trucks:
        return
    
    if len(present_trucks) < bridge_length:
        if sum(x[0] for x in present_trucks) + trucks[0] <= weight:
            present_trucks.append((trucks.popleft(), cnt))
