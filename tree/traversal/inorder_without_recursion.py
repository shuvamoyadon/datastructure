class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printinorder(root):

    s=[]
    temp=root
    while True:
        if temp :  ## thi will go on tll tmp is null
            s.append(temp)  #4 2 1
            temp=temp.left
        elif(s):
            temp=s.pop() # 4 is deleted from stack
            print(temp.data) # 4
            temp=temp.right ## it will print none as 4 has no right

        else:
            break



N=Node(1)
N.left=Node(2)
N.right=Node(3)
N.left.left=Node(4)
N.left.right=Node(5)

printinorder(N)