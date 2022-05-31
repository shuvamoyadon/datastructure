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


def test(root):
    curr=root
    pre=root
    while curr:
        #print('i',curr.data)
        if curr.left is not None:
            curr = curr.left
            print(curr.data)
        else:
            print('hi')
            curr=pre.left
            pre=curr.left
            #pre=curr.right
            print('p',curr.data)

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


inord = [ 4, 2, 5, 1, 3 ]
pre = [ 1, 2, 4, 5, 3]
n = len(inord)
printpostorderfrominorderpreorder(inord, pre, n)
print(end="\n")
ConstructTreeFromInorderAndPredorder(inord, pre, n)
