# My Approach
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def path(root, ans):
            if root: ans += str(root.val)
            if not root.left and not root.right: res.append(ans)
            if root.left: path(root.left, ans + '->')
            if root.right: path(root.right, ans + '->')

        res = []
        path(root, "")
        return res
