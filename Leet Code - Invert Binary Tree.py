# I solved it in a first go
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None or (root.left is None and root.right is None): return root
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
