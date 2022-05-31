class Tree:

    ##Create Node of a Tree
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None


    def preOrder(root):
        if not root:
            return
        print(root.data)
        Tree.preOrder(root.leftChild)
        Tree.preOrder(root.rightChild)

    def InOrder(root):
        if not root:
            return
        Tree.preOrder(root.leftChild)
        print(root.data)
        Tree.preOrder(root.rightChild)

    def PostOrder(root):
        if not root:
            return
        Tree.preOrder(root.leftChild)
        Tree.preOrder(root.rightChild)
        print(root.data)

bst=Tree("Drink")
leftnode=Tree("hot")
rightnode=Tree("cold")
bst.leftChild=leftnode
bst.rightChild=rightnode

bst.preOrder()
bst.InOrder()
bst.PostOrder()

##############################################################
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


# A function to do postorder tree traversal
def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# A function to do preorder tree traversal
def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left=Node(6)
root.left.left.right=Node(7)
root.right.left=Node(10)
root.right.right=Node(12)

print("Preorder traversal of binary tree is")
printPreorder(root)





