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
#printPreorder(root)

print('#######################')
Inx_min=-2**31
Inx_max=2**31


def findPostOrderUtil(pre, n, minval,
                      maxval, preIndex):
    # If entire preorder array is traversed
    # then return as no more element is left
    # to be added to post order array.
    if (preIndex[0] == n):
        return

    # If array element does not lie in
    # range specified, then it is not
    # part of current subtree.
    if (pre[preIndex[0]] < minval or
            pre[preIndex[0]] > maxval):
        return

    # Store current value, to be printed later,
    # after printing left and right subtrees.
    # Increment preIndex to find left and right
    # subtrees, and pass this updated value to
    # recursive calls.
    val = pre[preIndex[0]]
    preIndex[0] += 1

    # All elements with value between minval
    # and val lie in left subtree.
    findPostOrderUtil(pre, n, minval,
                      val, preIndex)

    # All elements with value between val
    # and maxval lie in right subtree.
    findPostOrderUtil(pre, n, val,
                      maxval, preIndex)

    print(val, end=" ")


pred = [40, 30, 35, 80, 100] ## output 35 30 100 80 40
preIndex =[0]
findPostOrderUtil(pred, len(pred), Inx_min,
                  Inx_max, preIndex)

post=[4,5,2,3,1]


