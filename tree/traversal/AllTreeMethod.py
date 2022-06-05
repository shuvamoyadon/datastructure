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
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)

def prnt_lvl_without_recursion_stack_inorder(root):
    curr=root
    while curr:
        if curr.left is None:
            print(curr.data) #4
            #print('curr.right',curr.right.data) #2
            curr = curr.right
        else:
            # Find the previous (prev) of curr
            prev = curr.left #4
           # print('prev',prev.data) #2 #4 #4
            while (prev.right is not None and prev.right != curr):
                prev = prev.right
                #print('jj',prev.data) #5

            # Make curr as right child of its prev
            if (prev.right is None):
                #print('assign prev.right',curr.data) #1 #2
                prev.right = curr
                curr = curr.left
                #print('new curr assign',curr.data) #2 #4

            # fix the right child of prev
            else:
                prev.right = None
                print(curr.data)
                curr = curr.right


def prnt_lvl_without_recursion_stack_preorder(root):
    curr=root
    while curr:
        if curr.left is None:
            print(curr.data) #4
            #print('curr.right',curr.right.data) #2
            curr = curr.right
        else:
            # Find the previous (prev) of curr
            prev = curr.left #4
           # print('prev',prev.data) #2 #4 #4
            while (prev.right is not None and prev.right != curr):
                prev = prev.right
                #print('jj',prev.data) #5

            # Make curr as right child of its prev
            if (prev.right is None):
                #print('assign prev.right',curr.data) #1 #2
                prev.right = curr
                print(curr.data)
                curr = curr.left
                #print('new curr assign',curr.data) #2 #4

            # fix the right child of prev
            else:
                prev.right = None
                curr = curr.right


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
def printpostorderfrominorderpreorder(inord,pre,n):
    #post order print  4, 5, 2, 3, 1
    root=search(inord,pre[0],n)
    #print('r',root,n)
    if root!=0:
        #print('ino',inord[0:root],'pre',pre[1:root+1],'root',root,'n',n)
        printpostorderfrominorderpreorder(inord[0:root],pre[1:root+1],root)

    #print("call1")
    if (root != n-1):
        #print('inside',root,n)
        #print('i********de',inord,pre,inord[root+1:n],'pre',pre[root+1:n],'n',n,root,n-root-1)
        printpostorderfrominorderpreorder(inord[root+1:n],pre[root+1:n],n-root-1)

    #print('re',pre[0])
    print(pre[0],end="")

def ConstructTreeFromInorderAndPredorder(inord,pre,n):
    #post order print  4, 5, 2, 3, 1
    root=search(inord,pre[0],n)
    #print(root)
    Nd=Node(inord[root])
    #print(inord[root])
    if root != 0:
       Nd.left=ConstructTreeFromInorderAndPredorder(inord[0:root],pre[1:root+1],root)

    if root!=n-1:
        Nd.right=ConstructTreeFromInorderAndPredorder(inord[root+1:n],pre[root+1:n],n-root-1)

    #print(Nd.data)
    printInorder(Nd)

#########################################################

def construct(start,end,pre,Pindex,d):
    ## base case
    if start > end:
        return None, Pindex

    #### get root from pre list and crete node
    root=Node(pre[Pindex])
    Pindex=Pindex+1

    ### get index from inorder dictionary
    index=d[root.data]

    ## now build the left tree and right tree
    root.left,Pindex=construct(start,index-1,pre,Pindex,d)
    root.right,Pindex=construct(index+1,end,pre,Pindex,d)

    return root,Pindex

def constructTree(inorder, preorder):
    # create a dictionary to efficiently find the index of any element in
    # a given inorder sequence
    d = {}
    for i, e in enumerate(inorder):
        d[e] = i

    # `pIndex` stores the index of the next unprocessed node in a preorder sequence;
    # start with the root node (present at 0th index)
    pIndex = 0

    ## return tuple get the first element as root
    return construct(0, len(inorder) - 1, preorder, pIndex, d)[0]

#########################################################################3
Inx_min=-2**31
Inx_max=2**31


def findPostOrderFromPreorder(pre, n, minval,
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
    findPostOrderFromPreorder(pre, n, minval,
                      val, preIndex)

    # All elements with value between val
    # and maxval lie in right subtree.
    findPostOrderFromPreorder(pre, n, val,
                      maxval, preIndex)

    print(val, end=" ")

#########################################################################
a=[]
def printPreorder(node):
    if node is None:
        return
    node.data
    printPreorder(node.left)
    printPreorder(node.right)
    return root

def inorderTrarray(root):

    if root is None:
        return
    inorderTrarray(root.left)
    #print(root.data)
    a.append(root.data)
    inorderTrarray(root.right)
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

#########################################################################

pred = [40, 30, 35, 80, 100] ## output 35 30 100 80 40
preIndex =[0]
findPostOrderFromPreorder(pred, len(pred), Inx_min,Inx_max,preIndex)
print('\n#################')

N=Node(1)
N.left=Node(2)
N.right=Node(3)
N.left.left=Node(4)
N.left.right=Node(5)

#print_lvl(N)
#prnt_lvl_without_recursion_stack_inorder(N)
prnt_lvl_without_recursion_stack_preorder(N)
#test(N)
##    1
 #  2    3
# 4   5

print('\n#################')
inord = [ 4, 2, 5, 1, 3 ]
pre = [ 1, 2, 4, 5, 3]
n = len(inord)
printpostorderfrominorderpreorder(inord, pre, n)
print(end="\n")

print('\n#################')
ConstructTreeFromInorderAndPredorder(inord, pre, n)

print('\n#################')
#####Another techniq from pre order and inorder using hash O(N) and O(N)
root=constructTree(inord, pre)
# traverse the constructed tree
print('\nThe preorder traversal is ', end='')
printInorder(root)
print('\n#################')

root = Node(1)  # 1
root.left = Node(2)  # / \
root.right = Node(3)  # 2     3
root.left.left = Node(4)  # / \ / \
root.left.right = Node(5)  # 4 5 6 7
root.right.left = Node(6)
root.right.right = Node(7)

print("Node preorder")
preord(printPreorder(root))
pre = printPreorder(root)
print("\n")
preord(nodeReplaceWithSuccessorAndPredecessor(pre,getSumofPreviouAndNext(inorderTrarray(root))))
