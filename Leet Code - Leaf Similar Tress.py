# My Approach
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaf(root: TreeNode, lst: list) -> list:
            if root is not None:
                if root.left is None and root.right is None:
                    lst.append(root.val)
                leaf(root.left, lst)
                leaf(root.right, lst)
            return lst

        lst1 = leaf(root1, list())
        lst2 = leaf(root2, list())
        if len(lst1) != len(lst2): return False
        return lst1 == lst2
