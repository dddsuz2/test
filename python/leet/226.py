from typing import Optional

from helper import Helper
from models import TreeNode

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        L = self.invertTree(root.right)
        R = self.invertTree(root.left)

        root.left = L
        root.right = R

        return root
    

if __name__ == "__main__":
    sol = Solution()
    helper = Helper()

    input = [4, 2, 7, 1, 3, 6, 9]
    input_tree = helper.list_to_tree(input)
    ans_tree = sol.invertTree(input_tree)
    ans_list = helper.tree_to_list(ans_tree)
    print(ans_list)
