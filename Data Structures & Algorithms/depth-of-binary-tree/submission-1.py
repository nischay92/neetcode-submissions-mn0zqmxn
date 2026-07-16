# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

        # iterative DFS
        depth = 0
        stack = [[root,1]]
        while stack:
            node, dep = stack.pop()
            if node:
                depth = max(depth, dep)
                stack.append([node.left, dep + 1])
                stack.append([node.right, dep + 1])
        return depth