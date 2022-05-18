
"""create a root node only


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data 

    def PrintTree(self):

        print(self.data)

root = Node(10)
root.PrintTree()

"""


from logging.handlers import DatagramHandler


class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data :
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)

                else :
                    self.left.insert(data)

            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)

                else :
                    self.right.insert(data)

        else :
            self.data = data

    def PrintTree(self):

        if self.left :
           self.left.PrintTree()

        print(self.data)
        if self.right :
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
