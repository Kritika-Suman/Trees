# My approach: Recursive - TC = O(n) & SC = O(n) in worst case and in avg case O(logn)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root, lst):
            if root is None: return lst
            inorder(root.left, lst)
            lst.append(root.val)
            inorder(root.right, lst)
            return lst

        return inorder(root, list())

#Better solution: Morris Traversal with TC = O(n) & SC = O(1)

# Step 1: Initialize current as root
# Step 2: While current is not NULL,
# If current does not have left child
#     a. Add current’s value
#     b. Go to the right, i.e., current = current.right
# Else
#     a. In current's left subtree, make current the right child of the rightmost node
#     b. Go to this left child, i.e., current = current.left

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lst = list()
        while root:
            if root.left:
                rt = root.left
                while rt.right:
                    rt = rt.right
                rt.right = root
                root = root.left
                rt.right.left = None
            else:
                lst.append(root.val)
                root = root.right
        return lst
