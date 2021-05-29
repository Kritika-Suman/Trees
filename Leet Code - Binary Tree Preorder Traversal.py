class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)

        res = list()
        preorder(root)
        return res
