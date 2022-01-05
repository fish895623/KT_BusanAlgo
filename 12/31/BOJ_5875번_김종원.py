# BOJ 5875번
s = "()(())))"
# ()(())()) --> 1
# (((()))) --> 1
# ()((()))) --> 1
# ()(()())) --> 1
# () 짝을 마춘거는 사라지고 
# (괄호가 마무리 되는 구간.)

# 왼쪽 3 -> 1개 주면 4
# 오른쪽 5 -> -1 하면 4

[1, 1, 2, 3, 3, 3, 3, 3]
[0, 1, 1, 1, 2, 3, 4, 5]

left_count , right_count = 0,0

left_stack, right_stack = [], []

left_list, right_list = [0]* len(s),[0]* len(s)

total_count =0

for i in range(len(s)):
    if s[i] == "(":
        left_count +=1
        total_count +=1
        left_stack.append(i)
    # 오른쪽 괄호만났을때
    else:
        right_count +=1
        # 오른쪽 괄호 만났을때 -1을 함으로써 왼쪽과 오른쪽의 합이 0으로 수립하고자 한다.
        total_count -=1 
        # 왼쪽 괄호가 오른쪽 괄호보다 앞에 있다면 쌍이 맞기에 left 스택에서 값을 pop한다.
        if left_stack:
            left_stack.pop()
        # 왼쪽괄호가 없는 상황에서 오른쪽 괄호가 먼저 있다면 right 스택에 담는다.
        else:
            right_stack.append(i)
    
    left_list[i] = left_count
    right_list[i] = right_count
    
print(left_list)
print(right_list)
print(total_count)
print("------")
print(left_stack)
print(right_stack)


# 주어진 S에서 ) 오른쪽 괄호가 왼쪽 괄호에 비해 많다.
if total_count <0:
    val = right_list[right_stack[0]]
    print(val)
elif total_count ==0:
    print(left_list[-1])