class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSame(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            return root1.val == root2.val and isSame(root1.left, root2.left) and isSame(root1.right, root2.right)

        if not subRoot: return True  # None is subtree of every tree
        if not root: return False  # a tree can not be a subtree of None
        if isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
