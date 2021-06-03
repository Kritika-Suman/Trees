# My approach - logically correct but inefficient

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        queue = [root]
        while queue:
            size = len(queue)
            level_queue = []
            i = 0
            while i<size:
                i+= 1
                node = queue.pop(0)
                if node.left: level_queue.append(node.left)
                else: level_queue.append(TreeNode(-1000))
                if node.right: level_queue.append(node.right)
                else: level_queue.append(TreeNode(-1000))
            x = 0
            y = len(level_queue)-1
            flag = y+1
            # print(level_queue)
            while x<y:
                if level_queue[x].val != level_queue[y].val: return False
                if level_queue[x].val == -1000: flag -= 1
                if level_queue[y].val == -1000: flag -= 1
                x += 1
                y -= 1
            if flag:
                queue = level_queue
        return True

# Recursive Approach

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(root1: TreeNode, root2: TreeNode) -> bool:
            if not root1 and not root2: return  True
            if not root1 or not root2: return False
            return root1.val == root2.val and symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)
        return symmetric(root, root)

# TC = O(N) and SC = O(N) in worst case

# Iterative Approach

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None: return True
        queue = [root, root]
        while queue:
            root1 =  queue.pop(0)
            root2 = queue.pop(0)
            if not root1 and not root2: continue
            if not root1 or not root2: return False
            if root1.val != root2.val: return False
            queue.append(root1.left)
            queue.append(root2.right)
            queue.append(root2.left)
            queue.append(root1.right)
        return True

# TC = O(N) and SC = O(N) in worst case
