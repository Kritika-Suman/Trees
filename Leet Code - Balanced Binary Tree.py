# My Approach

# class Solution:
#     def height(self, root):
#         if root is None: return 0
#         return 1 + max(self.height(root.left), self.height(root.right))
#
#     def isBalanced(self, root: TreeNode) -> bool:
#         if root is None: return True
#         queue = [root]
#         while queue:
#             level_size = len(queue)
#             level_queue = []
#             i = 0
#             while i<level_size:
#                 i += 1
#                 node = queue.pop(0)
#                 if node:
#                     lt = self.height(node.left)
#                     rt = self.height(node.right)
#                     if abs(lt-rt) > 1: return False
#                     level_queue.append(node.left)
#                     level_queue.append(node.right)
#             queue = level_queue
#         return True

# Efficient Approach

class Solution:
    def height(self, root):
        if root is None: return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None: return True
        lt = self.height(root.left)
        rt = self.height(root.right)
        return abs(lt - rt) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
