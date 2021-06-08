# My Approach - DFS

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Optimized Approach - BFS

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root: return depth
        queue = [root]
        while queue:
            depth += 1
            level_size = len(queue)
            i = 0
            while i<level_size:
                i+=1
                node = queue.pop(0)
                if not node.left and not node.right: return depth
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
