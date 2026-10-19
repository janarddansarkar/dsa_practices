# Linked Lists

A linked list stores nodes that point to the next node. No random access (O(n) to reach index i), but O(1) insert/delete
once you hold the node.

## Patterns
1. Dummy head node -- removes the special case of changing the head
2. Fast and slow pointers -- middle, cycle detection, k-th from end
3. Reverse in place -- three pointers: prev, curr, next
4. Merge two lists -- the base of merge sort and merge k lists


## Problems (easy to hard)

Work top to bottom. Each level adds one new idea on top of the last.

### Level 1 - Pointer basics
LeetCode 206.     Reverse Linked List                             -- iterative first, then recursive
LeetCode 21.      Merge Two Sorted Lists                          -- dummy head
LeetCode 876.     Middle of the Linked List                       -- slow / fast - DONE
LeetCode 141.     Linked List Cycle                               -- Floyd's slow / fast - DONE
LeetCode 83.      Remove Duplicates from Sorted List
LeetCode 203.     Remove Linked List Elements                     -- dummy head

### Level 2 - Two pointers and gaps
LeetCode 19.      Remove Nth Node From End of List                -- gap of n between pointers
LeetCode 160.     Intersection of Two Linked Lists                -- switch heads at the end
LeetCode 234.     Palindrome Linked List                          -- middle + reverse second half
LeetCode 142.     Linked List Cycle II                            -- where does the cycle start?
LeetCode 2.       Add Two Numbers                                 -- carry

### Level 3 - Rearranging
LeetCode 24.      Swap Nodes in Pairs
LeetCode 328.     Odd Even Linked List
LeetCode 61.      Rotate List
LeetCode 143.     Reorder List                                    -- middle + reverse + merge
LeetCode 148.     Sort List                                       -- merge sort

### Level 4 - Hard
LeetCode 25.      Reverse Nodes in k-Group
LeetCode 23.      Merge k Sorted Lists                            -- heap or divide and conquer
LeetCode 138.     Copy List with Random Pointer
LeetCode 146.     LRU Cache                                       -- hash map + doubly linked list
