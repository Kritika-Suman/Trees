# For sum of leaf nodes
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = 0
        if root:
            if not root.left and not root.right:
                ans += root.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
                ans += self.sumOfLeftLeaves(root.right)
        return ans

# For sum of left leaf nodes
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def LeftLeavesSum(root, flag):
            ans = 0
            if root:
                if not root.left and not root.right and flag:
                    ans += root.val
                else:
                    ans += LeftLeavesSum(root.left, True)
                    ans += LeftLeavesSum(root.right, False)
            return ans
        return LeftLeavesSum(root, False)
