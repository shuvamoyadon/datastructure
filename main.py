class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def printInorder(node):
    if (node == None):
        return

    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)

def search(inTree,preElement,n):
    for i in range(n):
        if inTree[i] == preElement:
            return i
    return -1


def construct(start, end, preorder, pIndex, d):
    # base case
    if start > end:
        print('hi')
        return None, pIndex

    # The next element in `preorder[]` will be the root node of subtree
    # formed by sequence represented by `inorder[start, end]`
    root = Node(preorder[pIndex])
    pIndex = pIndex + 1

    # get the index of the root node in inorder to determine the
    # left and right subtree boundary
    index = d[root.data]

    # recursively construct the left subtree
    root.left, pIndex = construct(start, index - 1, preorder, pIndex, d)

    # recursively construct the right subtree
    #root.right, pIndex = construct(index + 1, end, preorder, pIndex, d)

    # return current node
    return root, pIndex


# Construct a binary tree from inorder and preorder traversals.
# This function assumes that the input is valid
# i.e., given inorder and preorder sequence forms a binary tree
def constructTree(inorder, preorder):
    # create a dictionary to efficiently find the index of any element in
    # a given inorder sequence
    d = {}
    for i, e in enumerate(inorder):
        d[e] = i

    # `pIndex` stores the index of the next unprocessed node in a preorder sequence;
    # start with the root node (present at 0th index)
    pIndex = 0

    return construct(0, len(inorder) - 1, preorder, pIndex, d)[0]

#inord=[1,6,8,7]
#pre =[1,6,7,8]
inord = [ 4, 2, 5, 1, 3 ]
pre = [ 1, 2, 4, 5, 3]
n = len(inord)
root=constructTree(inord, pre)
# traverse the constructed tree
print('\nThe preorder traversal is ', end='')
printInorder(root)

#print('-----')
inord=[4,2,5]
#print(inord[2:3])
#print(pre[3+1:5])
#preIndex = [0]
#print(preIndex[0])
INT_MIN = -2**31
INT_MAX = 2**31
#print(INT_MIN)



