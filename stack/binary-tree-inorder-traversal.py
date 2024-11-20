# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, nodes):
        if not root: return nodes

        self.traverse(root.left, nodes)
        nodes.append(root.val)
        self.traverse(root.right, nodes)
        
        return nodes


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        nodes = []
        return self.traverse(root, nodes)

        

    