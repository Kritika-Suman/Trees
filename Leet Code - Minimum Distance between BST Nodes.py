# Same as Minimum Absolute Difference in BST

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        res = []
        inorder(root)
        i, diff = 1, res[-1]
        while i<len(res):
            diff = min(diff, res[i]-res[i-1])
            i += 1
        return diff
