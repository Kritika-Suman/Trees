# My Approach

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def checkCousins(root, parent, depth, key):
            info = []
            if root:
                if root.val == key:
                    info = [parent, depth]
                else:
                    temp = checkCousins(root.left, root, depth + 1, key)
                    if temp: info = temp
                    temp = checkCousins(root.right, root, depth + 1, key)
                    if temp: info = temp

            return info

        x_info = checkCousins(root, None, 0, x)
        y_info = checkCousins(root, None, 0, y)
        if x_info[1] == y_info[1]:
            if x_info[0].val != y_info[0].val:
                return True
        return False

# Efficient Solution

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parent_x, parent_y = None, None
        temp = TreeNode(-1)

        # At level 0 only root is there
        queue = [(root, temp)]

        while queue:  # To process each and every node
            level_size = len(queue)
            while level_size:  # For level wise processing
                node = queue.pop(0)
                level_size -= 1
                if node[0].val == x: parent_x = node[1].val
                if node[0].val == y: parent_y = node[1].val
                if node[0].left: queue.append((node[0].left, node[0]))
                if node[0].right: queue.append((node[0].right, node[0]))
                if parent_x and parent_y: break;
            # We can reach here either when level is exhausted or both parents are found
            # Both parents are found
            if parent_x and parent_y:
                if parent_x != parent_y: return True
            # One among the two parents are found
            if (parent_x and not parent_y) or (not parent_x and parent_y): return False
        # Neither x nor y is present in tree
        return False
