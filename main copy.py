class TreeNode:
    def __init__(self,v):
       self.value=v
       self.right=None
       self.left=None 
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,root,v):
        if root is None:
            return TreeNode(v)
        if v > root.value:
            root.right=self.insert(root.right,v)
        else:
            root.left=self.insert(root.left,v)
        return root
        


    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.value)
            self.inOrder(root.right)
    
    def preOrder(self,root):
        if root:
            print(root.value)
            self.preOrder(root.left)
            self.preOrder(root.right)
    
    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.value)


    def search(self,v,root=None):
        if root is None:
            return None
        
        if v == root.value:
            return root
        
        elif v > root.value:
            return self.search(v,root.right)
        
        else:
            return self.search(v,root.left)
        

x=True
while x == True:
    input1=input('What would you like to do?\n 1.Create Tree\n 2.Search value\n 3.Insert value\n 4.Exit\n')

    if input1 == '1':
        tree=BinarySearchTree()
        num=input('What root do you want? ')
        tree.root=TreeNode(num)

        num1=input('What is the 1st value? ')
        tree.insert(tree.root,num1)

        num2=input('What is the 2nd value? ')
        tree.insert(tree.root,num2)

        num3=input('What is the 3rd value? ')
        tree.insert(tree.root,num3)

        num4=input('What is the 4th value? ')
        tree.insert(tree.root,num4)

        num5=input('What is the 5th value? ')
        tree.insert(tree.root,num5)

        num6=input('What is the 6th value? ')
        tree.insert(tree.root,num6)

    elif input1 == '2':
        search=int(input('What value would you like to search? '))
        i=tree.search(search)
        if i:
            print('Key is found')
        else:
            print('Key is not found')

    elif input1 == '3':
        insert=input('What value would you like to insert? ')
        tree.insert(tree.root,insert)

    elif input1 == '4':
        x=False

    else:
        print('Please enter a valid number')













