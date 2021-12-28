"""
https://www.acmicpc.net/problem/4256

전위와 중위를 통해 후위를 만드는 것.

일단 전위를 가지고 트리를 만들어보자.

중위를 해서 트리를 만들어도 봐야하나?


전위 순회의 첫번째 값은 root이다.

전위 : 3,6,5,4,8,7,1,2

중위 : 5,6,8,4,3,1,2,7



"""

import sys
input = sys.stdin.readline

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def buildTree(pre_order, in_order):
    if in_order:

        index = in_order.index(pre_order.pop(0))

        node = Node(in_order[index])
        node.left = buildTree(pre_order, in_order[0:index])
        node.right = buildTree(pre_order, in_order[index + 1:])

        return node

def postorder(node):
    if node.left != None:
        postorder(node.left)
    if node.right != None:
        postorder(node.right)
    print(node.data, end = " ")

test_n = int(input())

for _ in range(test_n):

    n = int(input())

    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))


    tree_node = buildTree(pre_order, in_order)

    postorder(tree_node)
    print()
    












# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def left_append(self, data):
        
#         # 왼쪽에 이미 데이터가 존재한다면
#         if self.left != None:
#             self.data = self.left

#     def right_append(self, data):
#         pass

# test_n = int(input())

# for _ in range(test_n):
    
#     n = int(input())

#     pre_order = list(map(int, input().split()))
#     in_order = list(map(int, input().split()))

#     # pre_order의 첫번째 값은 루트노드
#     root = pre_order[0]

#     # 첫번째 값 넣기
#     tree_node = Node(root)

#     # 왼쪽 데이터
#     left_data = in_order[:in_order.index(root)]


#     # 오른쪽 데이터
#     right_data = in_order[in_order.index(root)+1 : ]

#     # 다음 값이 왼쪽에 있다.
#     if pre_order[1] in left_data:
#         root.left = Node(pre_order[1])
    

