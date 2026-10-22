# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        res=[]
        def get(node:TreeNode):
            if node is None:
                return
            get(node.left)
            res.append(node.val)
            get(node.right)
        get(root)
        pre=0
        next=1
        while next<len(res):
            if res[pre]>=res[next]:
                return False
            else:
                next+=1
                pre+=1
        return True
