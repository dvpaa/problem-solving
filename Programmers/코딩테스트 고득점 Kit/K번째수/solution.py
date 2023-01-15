def solution(array, commands):
    result = []
    for command in commands:
        arr = sorted(array[command[0]-1:command[1]])
        result.append(arr[command[2]-1])
    return result