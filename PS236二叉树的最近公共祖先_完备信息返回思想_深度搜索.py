# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node:'TreeNode'):
            if node is None:
                return  None,False,False
            left_ancestor,left_has_p,left_has_q=find(node.left)
            right_ancestor, right_has_p, right_has_q = find(node.right)
            has_p=left_has_p or right_has_p or node is p
            has_q = left_has_q or right_has_q or node is q
            ancestor=left_ancestor or right_ancestor
            if ancestor==None and has_p and has_q:
                ancestor=node
            return ancestor,has_p,has_q

        ancestor,_,_=find(root)
        return  ancestor

