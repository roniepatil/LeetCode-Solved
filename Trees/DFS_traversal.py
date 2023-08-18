class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val, end=" ")
        printInorder(root.right)

def printPreorder(root):
    if root:
        print(root.val, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end= " ")






if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("Inorder traversal of binary tree is")
    printInorder(root)

    # Function call
    print("\nPreorder traversal of binary tree is")
    printPreorder(root)

    # Function call
    print("\nPostorder traversal of binary tree is")
    printPostorder(root)

    

