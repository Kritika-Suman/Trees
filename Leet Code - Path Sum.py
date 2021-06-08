class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            targetSum -= root.val
            if not root.left and not root.right:
                if targetSum == 0:
                    return True
                else:
                    return False
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

        return False
