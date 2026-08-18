# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetric(t1,t2):
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            if t1.val == t2.val:
                return checkSymmetric(t1.left, t2.right) and checkSymmetric(t1.right, t2.left)
            return False
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        return checkSymmetric(root.left, root.right)