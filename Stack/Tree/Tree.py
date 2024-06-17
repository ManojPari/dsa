class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.ans = []

    def inorderTraversal(self, root):
        if not root:
            return
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        return self.ans

# Example of creating a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

# Create the nodes
debugger
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
t = TreeNode
t.inorderTraversal(root)

