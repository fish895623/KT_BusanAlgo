s = "()(())))"

arr = list(s)
N = len(arr)

# 왼쪽 괄호 갯수를 카운트 / 오른쪽 괄호 갯수를 카운트
left_bracket = 0
right_bracket = 0

# 왼쪽괄호가 많을 수 있고 오른쪽 괄호가 많을 수 있다. 이를 표현하는 변수
total_sum = 0

# 왼쪽 괄호 또는 오른쪽 괄호를 만나면 스택에 push 한다.
left_stack = []
right_stack = []

# 전체 N개의 자리 순서대로 왼쪽 또는 오른쪽 괄호의 갯수 정보를 나타냄
left_list = [0]*N
right_list = [0]*N
 
for i in range(N):
    if arr[i] == '(':
        left_bracket += 1
        total_sum += 1
        left_stack.append(i)
    else:
        right_bracket += 1
        total_sum -= 1
        if left_stack:
            left_stack.pop()
        else:
            right_stack.append(i)
    
    left_list[i] = left_bracket
    right_list[i] = right_bracket

print(right_stack)
# 왼쪽괄호가 많으면 +
if total_sum > 0:
    print(left_list[-1] - left_list[left_stack[-1]]+1)
# 오른쪽 괄호가 많으면  -
elif total_sum <0:
    print(right_list[right_stack[0]])
else:
    print(0)