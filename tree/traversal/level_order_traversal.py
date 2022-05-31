class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def print_lvl(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while len(q) > 0:
            print(q[0].data)
            root=q.pop(0)
            print('hi',root.data)
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)




N=Node(1)
N.left=Node(2)
N.right=Node(3)
N.left.left=Node(4)
N.right.right=Node(5)

##    1
 #  2    3
# 4   5

print_lvl(N)