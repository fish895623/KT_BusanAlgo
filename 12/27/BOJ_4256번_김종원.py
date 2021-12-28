# BOJ_4256번

def pre_in_to_post(pre_list,in_list):
    if pre_list:
        root = pre_list[0]
        mid = in_list.index(root)
        pre_in_to_post(pre_list[1:mid+1], in_list[:mid])
        pre_in_to_post(pre_list[mid+1 :], in_list[mid+1:])
        print(root, end=" ")

pre_order = [3,2,1,4]
in_order = [2,3,4,1]

pre_in_to_post(pre_order, in_order)