 def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    elif len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    elif len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return
        
    root = preorder[0]
    inorderidx = inorder.index(root)
    postorder(preorder[1:inorderidx+1], inorder[:inorderidx])
    postorder(preorder[inorderidx+1:], inorder[inorderidx+1:])
    print(preorder[0], end=' ')

n = int(input())
for _ in range(n):
    m = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    postorder(preorder, inorder)
    print()