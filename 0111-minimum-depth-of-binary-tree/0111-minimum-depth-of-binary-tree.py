# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return depth
        queue = deque()
        queue.append(root)
        
        while queue:
            depth += 1
            level = len(queue)
            for _ in range(level):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth