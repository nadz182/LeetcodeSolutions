# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        def dfs(currentNode, requiredSum, currentPath, allPaths):
            if currentNode is None:
                return
            
            currentPath.append(currentNode.val)
            
            if currentNode.val == requiredSum and currentNode.left is None and currentNode.right is None:
                allPaths.append(list(currentPath))
            else:
                dfs(currentNode.left, requiredSum-currentNode.val, currentPath, allPaths)
                dfs(currentNode.right, requiredSum-currentNode.val, currentPath, allPaths)
            del currentPath[-1]
        
        
        allPaths = []
        dfs(root, targetSum, [], allPaths)
        return allPaths