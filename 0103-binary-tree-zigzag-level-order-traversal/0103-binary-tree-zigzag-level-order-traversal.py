# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if root is None:
            return result
        leftToRight = True
        queue = deque()
        queue.append(root)
        
        while queue:
            level = len(queue)
            currentLevel = deque()
            
            for _ in range(level):
                currentNode = queue.popleft()
                if leftToRight:
                    currentLevel.append(currentNode.val)
                else:
                    currentLevel.appendleft(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(list(currentLevel))
            leftToRight = not leftToRight
        return result