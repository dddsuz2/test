from collections import deque
from typing import List, Optional

from models import TreeNode

class Helper:
    def tree_to_list(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            current = queue.popleft()
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)

        return result
    
    def list_to_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1

        while queue and i < len(values):
            current = queue.popleft()

            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1

            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1

        return root
