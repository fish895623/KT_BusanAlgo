# class Nodee:
#     def __init__(self,x):
#         self.current = x
#         self.left = 0
#         self.right = 0
#     def leftNode(self,fx):
#         self.left = fx
#     def rightNode(self,rx):
#         self.right = rx

# no = Nodee()
# node = int(input())

node = 4
mid = [3,2,1,4]
front = [2,3,4,1]

root = [mid[0]]
right_root = front[-1]

left_tree  = []
right_tree = []
for x in range(len(front)):
    if front[x] == root[0]:
        break
    left_tree.append(front[x])
right_tree = front[x+1:]

print(left_tree)
print(root)
print(right_tree)
print(right_root)
# if len(right_tree) !=1:


