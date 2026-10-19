# Trees and Binary Search Trees

A tree is recursive by nature: solve for the left subtree, the right subtree, then combine at the root.

## Patterns
1. DFS (preorder / inorder / postorder) -- recursion
2. BFS (level order) -- queue
3. Return a value up + update a global answer (diameter, max path sum)
4. BST property: inorder traversal is sorted


## Problems (easy to hard)

Work top to bottom. Each level adds one new idea on top of the last.

### Level 1 - Traversals and simple recursion
LeetCode 104.     Maximum Depth of Binary Tree
LeetCode 100.     Same Tree
LeetCode 226.     Invert Binary Tree
LeetCode 101.     Symmetric Tree
LeetCode 94.      Binary Tree Inorder Traversal                   -- recursive, then iterative
LeetCode 144.     Binary Tree Preorder Traversal
LeetCode 145.     Binary Tree Postorder Traversal
LeetCode 102.     Binary Tree Level Order Traversal

### Level 2 - Combine children's answers
LeetCode 110.     Balanced Binary Tree
LeetCode 543.     Diameter of Binary Tree                         -- return height, update global
LeetCode 112.     Path Sum
LeetCode 199.     Binary Tree Right Side View
LeetCode 103.     Binary Tree Zigzag Level Order Traversal

### Level 3 - BST
Idea: use left < root < right to discard half the tree.

LeetCode 700.     Search in a Binary Search Tree
LeetCode 701.     Insert into a Binary Search Tree
LeetCode 98.      Validate Binary Search Tree                     -- pass (low, high) bounds
LeetCode 230.     Kth Smallest Element in a BST                   -- inorder
LeetCode 235.     Lowest Common Ancestor of a BST
LeetCode 108.     Convert Sorted Array to Binary Search Tree
LeetCode 450.     Delete Node in a BST
LeetCode 669.     Trim a Binary Search Tree

### Level 4 - Construction and harder recursion
LeetCode 236.     Lowest Common Ancestor of a Binary Tree
LeetCode 105.     Construct Binary Tree from Preorder and Inorder Traversal
LeetCode 114.     Flatten Binary Tree to Linked List
LeetCode 437.     Path Sum III

### Level 5 - Hard
LeetCode 124.     Binary Tree Maximum Path Sum
LeetCode 297.     Serialize and Deserialize Binary Tree
