# My first approach
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        def binarySearch(arr, key, srt, end):
            if srt > end: return False
            mid = (srt + end) // 2

            if arr[mid] == key: return True
            if arr[mid] > key:
                return binarySearch(arr, key, srt, mid - 1)
            else:
                return binarySearch(arr, key, mid + 1, end)

        res = []
        inorder(root)

        srt, end, flag = 1, len(res) - 1, 0

        for x in res:
            if binarySearch(res, k - x, srt, end):
                flag = 1
                break
            srt += 1
        return flag
