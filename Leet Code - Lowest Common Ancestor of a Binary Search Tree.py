# Approach 1: This is for Binary Tree (work for BST too but can be optimised)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: return None
        if root.val == p.val or root.val == q.val: return root
        lt = self.lowestCommonAncestor(root.left, p, q)
        rt = self.lowestCommonAncestor(root.right, p, q)
        if lt and rt: return root
        if lt: return lt
        else: return rt
        return None

# Approach 2: Recursive approach utilising the BST property

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

# TC : O(N)
# SC : O(N)

#Approach 3: Itervative approach utilising the BST property

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val>p.val and root.val>q.val:
                root = root.left
            elif root.val<p.val and root.val<q.val:
                root = root.right
            else: return root

# TC : O(N)
# SC : O(N)
