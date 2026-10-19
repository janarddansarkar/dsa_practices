## Hash Table (Hash Map / Dictionary)

A hash table is a data structure that implements an associative array — a structure that maps keys to values 
using a **hash function** to compute an index into an array of buckets or slots.

### Key Properties
- **Fast lookups**: O(1) average time complexity
- **Key-value storage**: Each key maps to exactly one value
- **In Python**: Implemented as `dict`

### Simple Example

```python
# Create a hash table
student_grades = {}

# Insert/Update (O(1))
student_grades["Alice"] = 95
student_grades["Bob"] = 87

# Lookup (O(1))
print(student_grades["Alice"])  # Output: 95

# Delete (O(1))
del student_grades["Bob"]

# Check if key exists
if "Alice" in student_grades:
    print("Alice found")
```

### Why Hash Tables?
Instead of searching through a list in O(n) time, hash tables give you instant access to any value by its key in O(1) 
average time.

### Under the Hood
1. Hash function converts key → index
2. Value stored at that index
3. Collisions handled via chaining or open addressing


## Problems (easy to hard)

Work top to bottom. Each level adds one new idea on top of the last.

### Level 1 - Lookup and membership
Idea: turn an O(n) search into an O(1) lookup.

LeetCode 1.       Two Sum  - DONE
LeetCode 217.     Contains Duplicate
LeetCode 242.     Valid Anagram
LeetCode 383.     Ransom Note
LeetCode 205.     Isomorphic Strings
LeetCode 290.     Word Pattern

### Level 2 - Counting and grouping
Idea: pick a key that is the same for everything you want grouped.

LeetCode 49.      Group Anagrams
LeetCode 347.     Top K Frequent Elements
LeetCode 128.     Longest Consecutive Sequence  - DONE
LeetCode 36.      Valid Sudoku                                    -- sets for rows, cols, boxes
LeetCode 454.     4Sum II                                         -- split into two halves

### Level 3 - Prefix sum + hash map
Idea: store 'prefix seen so far' to find a subarray ending here.

LeetCode 560.     Subarray Sum Equals K  - DONE
LeetCode 525.     Contiguous Array
LeetCode 974.     Subarray Sums Divisible by K                    -- store prefix % k

### Level 4 - Design with hashing
Idea: combine a hash map with another structure.

LeetCode 380.     Insert Delete GetRandom O(1)                    -- map + list
LeetCode 146.     LRU Cache                                       -- map + doubly linked list
LeetCode 981.     Time Based Key-Value Store                      -- map + binary search
LeetCode 138.     Copy List with Random Pointer                   -- old node -> new node map
LeetCode 895.     Maximum Frequency Stack                         -- hard: map of stacks
