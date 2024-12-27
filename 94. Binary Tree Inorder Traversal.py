# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        # Идем по дереву
        while current or stack:
            # Идем по левому поддереву до самого конца
            while current:
                stack.append(current)
                current = current.left
            
            # Вырезаем узел из стека, обрабатываем его
            current = stack.pop()
            result.append(current.val)
            
            # Переходим к правому поддереву
            current = current.right
        
        return result
