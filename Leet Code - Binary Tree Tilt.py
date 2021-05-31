class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def tilt(root, ans):
            if root is None: return 0;
            if not root.left and not root.right: return root.val
            lt = tilt(root.left, ans)
            rt = tilt(root.right, ans)
            ans.append(abs(lt - rt))
            # print(ans)
            return lt + root.val + rt

        ans = []
        tilt(root, ans)
        return sum(ans)
