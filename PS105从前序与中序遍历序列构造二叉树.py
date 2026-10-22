# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return  None
        node=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        left_preorder=preorder[1:index+1]
        left_inorder=inorder[:index]
        right_preorder=preorder[index+1:]
        right_inorder=inorder[index+1:]
        node.left= self.buildTree(left_preorder, left_inorder)
        node.right=self.buildTree(right_preorder,right_inorder)
        return node

