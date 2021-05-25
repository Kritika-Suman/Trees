# I was able to print sum of all the binary numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binarySum(self, root: TreeNode, stack: list) -> int:
        if root is None:
            st = stack.copy()
            ans = 0
            i = 1
            while len(st):
                x = st[-1]
                st.pop(-1)
                ans += x * i
                i = i << 1
            return ans

        stack.append(root.val)
        res = self.binarySum(root.left, stack) + self.binarySum(root.right, stack)
        stack.pop(-1)
        return res

    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = []
        return self.binarySum(root, stack) // 2

# Correct Solution:
class Solution:
    def binarySum(self, root, ans):
        if root is None:
            return 0
        ans = (ans << 1) + root.val
        if root.left is None and root.right is None:
            print(ans)
            return ans
        return self.binarySum(root.left, ans) + self.binarySum(root.right, ans)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.binarySum(root, 0)
