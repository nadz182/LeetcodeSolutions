# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, targetSum, currentPath):
            if node is None:
                return 0
            
            pathsum, count = 0,0
            currentPath.append(node.val)
            
            for i in range(len(currentPath)-1, -1, -1):
                pathsum += currentPath[i]
                
                if pathsum == targetSum:
                    count += 1
            count += dfs(node.left, targetSum, currentPath)
            count += dfs(node.right, targetSum, currentPath)      
            
            del currentPath[-1]
            return count
        
        return dfs(root, targetSum , [])