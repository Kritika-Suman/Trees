class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def BST(nums, srt, end):
            if (srt>end): return None
            mid = (srt+end)//2
            root = TreeNode(nums[mid])
            root.left = BST(nums, srt, mid-1)
            root.right = BST(nums, mid+1, end)
            return root
        return BST(nums, 0, len(nums)-1)
