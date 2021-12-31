# BOJ 4256번
# 문제 예시 1  >> 성공
# pre_list = [3,2,1,4]
# in_list = [2,3,4,1]

# 문제 예시 2 >> 성공
# pre_list = [3,6,5,4,8,7,1,2]
# in_list = [5,6,8,4,3,1,2,7]

def pre_in_trans(pre_list, in_list):
    if pre_list:
        root = pre_list[0]
        mid = in_list.index(root)
        pre_in_trans(pre_list[1: mid+1], in_list[:mid])
        pre_in_trans(pre_list[mid+1:], in_list[mid+1:])
        print(root,end=" ")

T = int(input())
for i in range(T):
    node = int(input())
    pre_list = list(map(int,input().split()))
    in_list = list(map(int,input().split()))
    pre_in_trans(pre_list,in_list)
    print()