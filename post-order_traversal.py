

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else :
                if self.right is None:
                    self.right = Node(data)
                else:

                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()

            print( self.data)

            if self.right:
                self.right.PrintTree()


    def postorderTraversal(self, root):

        res = []
        if root :
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal((root.right))
            res.append(root.data)

        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.postorderTraversal(root))