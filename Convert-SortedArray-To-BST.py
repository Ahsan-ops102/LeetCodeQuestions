# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        middle = len(nums) // 2

        new_node = TreeNode(nums[middle])
        left = self.sortedArrayToBST(nums[:middle]) 
        right = self.sortedArrayToBST(nums[middle+1:])
        new_node.left = left
        new_node.right = right
        return new_node