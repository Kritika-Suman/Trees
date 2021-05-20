# My Approach - naive one - I didn't utilise the property of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return root

        if root.val != val:
            ans = self.searchBST(root.left, val)
            if ans:
                return ans
            else:
                ans = self.searchBST(root.right, val)
                if ans:
                    return ans
                else:
                    None

        else:
            return root

# Approach 2- when I used the BST property it reduced my run time and memory usage too
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return root

        if root.val != val:

            if root.val < val:
                return self.searchBST(root.right, val)
            else:
                return self.searchBST(root.left, val)

        else:
            return root


