n = int(input())
m = int(input())
buttons = [True] * 10 

if m != 0:
    broken_buttons = list(map(int, input().split()))
    
    for broken_button in broken_buttons:
        buttons[broken_button] = False


def is_vaild(target):
    for s in str(target):
        if not buttons[int(s)]:
            return False
    return True

    
def search_min_vaild_num(target, stand):
    for i in range(stand):
        if target - i < 0:
            break
        
        if is_vaild(target-i):
            return target-i
            
    return float("inf")


def search_max_vaild_num(target, stand):
    for i in range(stand):
        if is_vaild(target+i):
            return target+i
    return float("inf")
    
    
def calculate_num(target, num):
    if num == float("inf"):
        return num
    return len(str(num)) + abs(target-num)
    

stand = abs(n - 100)
print(min(calculate_num(n, search_min_vaild_num(n, stand)), 
        calculate_num(n, search_max_vaild_num(n, stand)), 
        stand))
