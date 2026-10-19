## Basic Syntax of Recursion
#### Every recursive function has two parts:
    - Base Case → Stops the recursion.
    - Recursive Case → Calls itself on a smaller version of the problem.
#### General template:
    ```python
    def recursive_function(parameters):
        # Base case
        if stopping_condition:
            return answer
    
        # Work (optional)
    
        # Recursive call
        return recursive_function(smaller_problem)
    ```


1. In recursion, we should have a base case.
ex: 4! = 4 x 3!
       = 4 x 3 x 2!
       = 4 x 3 x 2 x 1!
       = 4 x 3 x 2 x 1
  Here, 1! = 1 is the base case

2. Base case loi goi thakute Problem tu smaller hoi hoi goi thakibo lage. As in the above example, ami 4! k vagi vagi
  last t 1! loi goi palu.

3. Backtracking :
Printing from start to end in the Normal approach
printing is started in the end and ended in the starting is back tracking. i.e., actual code execution tu last
r falor pora start hoi. 


In normal recursion things happens while going in forward pass, while
in backtracking, things happens in coming back, that's why the term backtracking.

## Recursion patterns (learning order)

1. Basic recursion         -- one call, shrink the input by 1 (or half), base case + work
2. Recursion on structures -- linked list / tree (the structure is already recursive)
3. Subsequences / Subsets  -- pick / not-pick at every index
4. Combinations            -- pick / not-pick with unlimited reuse or a target
5. Permutations            -- swap or used[] array
6. Grid / String backtracking -- choose, explore, un-choose
7. Hard backtracking       -- pruning + constraint checks

## Golden Rules:

1. Write the base case first. Ask: "what is the smallest input I can answer directly?"
2. Trust the recursion. Assume f(n-1) already works, only decide how to use its answer.
3. Every call must move closer to the base case.
4. For backtracking: choose -> explore -> un-choose (undo the change after the recursive call returns).
5. Draw the recursion tree for a small input before coding. Count the branches to estimate complexity.

## Problems

### Level 1 - Basic recursion (Easy)
LeetCode 509.     Fibonacci Number
LeetCode 70.      Climbing Stairs
LeetCode 344.     Reverse String                       -- two-pointer recursion
LeetCode 231.     Power of Two
LeetCode 326.     Power of Three
LeetCode 50.      Pow(x, n)                            -- fast exponentiation, halve the power
LeetCode 1137.    N-th Tribonacci Number
LeetCode 258.     Add Digits                           -- digit recursion
LeetCode 779.     K-th Symbol in Grammar               -- recursion on a pattern

### Level 2 - Recursion on Linked List / Tree (Easy to Medium)
LeetCode 206.     Reverse Linked List                  -- recursive version
LeetCode 21.      Merge Two Sorted Lists
LeetCode 24.      Swap Nodes in Pairs
LeetCode 83.      Remove Duplicates from Sorted List
LeetCode 104.     Maximum Depth of Binary Tree
LeetCode 100.     Same Tree
LeetCode 226.     Invert Binary Tree
LeetCode 112.     Path Sum

### Level 3 - Subsequences / Subsets (pick - not pick)
LeetCode 78.      Subsets                              -- same idea as 6.generate_all_subsequence
LeetCode 90.      Subsets II                           -- skip duplicates
LeetCode 784.     Letter Case Permutation
LeetCode 494.     Target Sum                           -- same idea as 7/8 (subsequence with sum k)
LeetCode 17.      Letter Combinations of a Phone Number
LeetCode 22.      Generate Parentheses

### Level 4 - Combinations
LeetCode 77.      Combinations
LeetCode 39.      Combination Sum                      -- reuse same element
LeetCode 40.      Combination Sum II                   -- no reuse, skip duplicates
LeetCode 216.     Combination Sum III
LeetCode 131.     Palindrome Partitioning
LeetCode 93.      Restore IP Addresses

### Level 5 - Permutations
LeetCode 46.      Permutations
LeetCode 47.      Permutations II                      -- duplicates
LeetCode 60.      Permutation Sequence                 -- (Hard) k-th permutation without generating all

### Level 6 - Grid / String backtracking (Medium)
LeetCode 79.      Word Search
LeetCode 1219.    Path with Maximum Gold
LeetCode 980.     Unique Paths III                     -- (Hard)
LeetCode 241.     Different Ways to Add Parentheses    -- divide and conquer recursion
LeetCode 95.      Unique Binary Search Trees II        -- build all trees recursively

### Level 7 - Hard backtracking
LeetCode 51.      N-Queens
LeetCode 52.      N-Queens II
LeetCode 37.      Sudoku Solver
LeetCode 140.     Word Break II
LeetCode 282.     Expression Add Operators
LeetCode 698.     Partition to K Equal Sum Subsets
LeetCode 679.     24 Game
