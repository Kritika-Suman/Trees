# My Approach

class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def preorder(root, ans):
            ans = ans + str(root.val)
            if root.left:
                ans += '('
                ans = preorder(root.left, ans)
                ans += ')'
                # if root.right is None: ans += '()'

            if root.right:
                if root.left is None: ans += '()'
                ans += '('
                ans = preorder(root.right, ans)
                ans += ')'

            return ans

        if root:
            return preorder(root, "")
        else:
            return ""
