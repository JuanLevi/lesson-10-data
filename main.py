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
        


    def minValueNode(self,node):
        current=node
        while current.left is not None:
            current = current.left
        return current
    


    def deleteValue(self,root,v):
        if root == None:
            return root
        
        if v < root.value:
            root.left=self.deleteValue(root.left,v)

        elif v > root.value:
            root.right=self.deleteValue(root.right,v)
    

        else: #1 child
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            #2 children
            temp=self.minValueNode(root.right)
            root.value=temp.value
            root.right=self.deleteValue(root.right,temp.value)
        return root
    

    def delete(self,v):
        self.root=self.deleteValue(self.root,v)

    




tree=BinarySearchTree()

tree.root=TreeNode(10)

tree.insert(tree.root,5)
tree.insert(tree.root,1)
tree.insert(tree.root,8)
tree.insert(tree.root,17)
tree.insert(tree.root,12)
tree.insert(tree.root,21)
tree.insert(tree.root,25)


tree.inOrder(tree.root)


tree.delete(5)
print('\n')
tree.inOrder(tree.root)

tree.delete(21)
print('\n')
tree.inOrder(tree.root)

tree.delete(1)
print('\n')
tree.inOrder(tree.root)





