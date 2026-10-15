# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def max_deep(node:TreeNode):
            if not node:
                return 0
            else:
                node.val=max(max_deep(node.left),max_deep(node.right))+1
            return node.val
        return max_deep(root)
