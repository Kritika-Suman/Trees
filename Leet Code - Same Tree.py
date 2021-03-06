class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Checking whether root is same or not
        if p is None and q is None: return True
        if p is None and q is not None: return False
        if p is not None and q is None: return False
        if p.val != q.val: return False
        # As root is same now check boot children are same or not which is the same ques for           # root
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
