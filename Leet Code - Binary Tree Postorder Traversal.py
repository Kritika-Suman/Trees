# Preorder: Root -> Left -> Right
# Inorder: Left -> Root -> Right
# Postorder: Left -> Right -> Root
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):
            if root:
                    postorder(root.left)
                    postorder(root.right)
                    lst.append(root.val)
        lst = list()
        postorder(root)
        return lst
