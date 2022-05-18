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

bst=Tree("Drink")
leftnode=Tree("hot")
rightnode=Tree("cold")
bst.leftChild=leftnode
bst.rightChild=rightnode

bst.preOrder()
bst.InOrder()





