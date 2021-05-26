# This was the first time I was working with n ary tree, I was clue less abt this thing but had a rough idea abt how to
# solve it, I referred the net and got the logic, I am glad that I attempted myself in python 3 and got it correct the first
# time.
# Little improvements matters :)

class Solution:
    def depth(self, root: 'Node', maxDepth: int) -> int:
        if root is None: return 0
        maxDepth += 1
        if root.children is None:
            return maxDepth
        temp = maxDepth
        for node in root.children:
            temp = max(self.depth(node, maxDepth), temp)
        return temp

    def maxDepth(self, root: 'Node') -> int:
        return self.depth(root, 0)