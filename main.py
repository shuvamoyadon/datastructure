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

def printPreorder(node):
    if node is None:
        return
    node.data
    printPreorder(node.left)
    printPreorder(node.right)
    return root

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
    root.right, pIndex = construct(index + 1, end, preorder, pIndex, d)

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
print('\nThe Inorder traversal is ', end='')
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



Inx_min=-2**31
Inx_max=2**31

def findPostOrderUtil(pre, n, minval,
                      maxval, preIndex):

    if (preIndex == n):
        return

    if (pre[preIndex] < minval or
            pre[preIndex] > maxval):
        return
    #print('pre', pre[preIndex])
    val = pre[preIndex]
    preIndex += 1

    findPostOrderUtil(pre, n, minval,val, preIndex)
    #
    # # All elements with value between val
    # # and maxval lie in right subtree.
    findPostOrderUtil(pre, n, val,maxval, preIndex)
    #
    print(val, end=" ")


pre = [40, 30, 35, 80, 100] ## output 35 30 100 80 40
preIndex =0
findPostOrderUtil(pre, len(pre), Inx_min,
                  Inx_max, preIndex)

def recu(n,a):
    if a[0] > n:
        return
    a[0]+=1
    val=a[0]
    print('val',val)
    recu(n,a)
    recu(n-1,a)
    print(val)

a=[0]
recu(5,a)
print('#############')
def recu1(n,a):
    if a > n:
        return
    a+=1
    val=a
    print('val',val)
    recu1(n,a)
    recu1(n-1,a)
    print(val)

a=0
recu1(5,a)

a=[]
def inorderTr(root):

    if root is None:
        return
    inorderTr(root.left)
    #print(root.data)
    a.append(root.data)
    inorderTr(root.right)
    return a

def nodeReplaceWithSuccessorAndPredecessor(root,dic):

    if root is None:
        return

    #print(root.data, dic[root.data])
    root.data = dic[root.data]
    nodeReplaceWithSuccessorAndPredecessor(root.left,dic)
    nodeReplaceWithSuccessorAndPredecessor(root.right, dic)
    return root

def getSumofPreviouAndNext(data):
    le=len(data)
    dict={}
    for i in range(0,len(data)):
           if i ==0:
              curr=data[i]
              pre =0
              next=data[i+1]
              sum=pre+next
              dict[curr]=sum
           elif(i==le-1):
               curr = data[i]
               pre=data[i-1]
               next=0
               sum = pre + next
               dict[curr] = sum
           else:
               curr = data[i]
               pre=data[i-1]
               next=data[i+1]
               sum = pre + next
               dict[curr] = sum

           #sm.append(sum)
    return dict

def preord(node):
    if node is None:
        return

    print(node.data,end=" ")
    preord(node.left)
    preord(node.right)


print("################################")
if __name__ == '__main__':
    # binary tree formation
    root = Node(1)  # 1
    root.left = Node(2)  # / \
    root.right = Node(3)  # 2     3
    root.left.left = Node(4)  # / \ / \
    root.left.right = Node(5)  # 4 5 6 7
    root.right.left = Node(6)
    root.right.right = Node(7)


    print("Node preorder")
    preord(printPreorder(root))
    pre=printPreorder(root)
    print("\n")
    preord(nodeReplaceWithSuccessorAndPredecessor(pre,getSumofPreviouAndNext(inorderTr(root))))




