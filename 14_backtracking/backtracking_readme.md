# Backtracking

Backtracking is an algorithmic technique that builds a solution step by
step. If a partial solution cannot lead to a valid answer, the algorithm
**undoes the last choice** and tries another option.

## Key Concepts

-   **Choose:** Make one possible choice.
-   **Explore:** Continue recursively with that choice.
-   **Undo:** Restore the state before trying the next choice.
-   **Base case:** Record or return a solution when the required
    condition is met.
-   **Pruning:** Stop exploring a branch as soon as it cannot produce a
    valid solution.

A common pattern is:

``` python
def backtrack(state):
    if is_complete(state):
        save_solution(state)
        return

    for choice in available_choices(state):
        make_choice(state, choice)
        backtrack(state)
        undo_choice(state)
```

The exact structure varies by problem. Some problems return the first
valid answer, while others collect every valid solution.

## Problems (easy to hard)

Work top to bottom. Each level adds exactly one new idea on top of the last.

### Level 1 - Pick / not pick (Subsets)
Idea: at every index either take the element or skip it.

LeetCode 78.      Subsets
LeetCode 784.     Letter Case Permutation
LeetCode 17.      Letter Combinations of a Phone Number
LeetCode 401.     Binary Watch

### Level 2 - Loop over choices (Permutations)
Idea: at each step try every unused element; undo `used[]` and `path` after returning.

LeetCode 46.      Permutations
LeetCode 1079.    Letter Tile Possibilities
LeetCode 526.     Beautiful Arrangement

### Level 3 - Combinations and targets
Idea: pass a start index so order doesn't matter; pass a remaining target so you can prune.

LeetCode 77.      Combinations
LeetCode 216.     Combination Sum III
LeetCode 39.      Combination Sum                      -- reuse the same element
LeetCode 22.      Generate Parentheses                 -- prune with open/close counts

### Level 4 - Handling duplicates
Idea: sort first, then skip `nums[i] == nums[i-1]` at the same recursion level.

LeetCode 90.      Subsets II
LeetCode 47.      Permutations II
LeetCode 40.      Combination Sum II

### Level 5 - Partitioning strings
Idea: choose where to cut; only recurse if the piece is valid.

LeetCode 131.     Palindrome Partitioning
LeetCode 93.      Restore IP Addresses

### Level 6 - Grid and path problems
Idea: mark the cell visited, explore 4 directions, then unmark it.

LeetCode 79.      Word Search
Rat in a Maze     -- classic, no single LeetCode ID
LeetCode 980.     Unique Paths III                     -- (Hard)
LeetCode 212.     Word Search II                       -- (Hard) backtracking + trie

### Level 7 - Constraint satisfaction (Hard)
Idea: keep row/column/box state so validity checks are O(1); prune early.

LeetCode 51.      N-Queens
LeetCode 52.      N-Queens II
LeetCode 37.      Sudoku Solver
LeetCode 473.     Matchsticks to Square
LeetCode 698.     Partition to K Equal Sum Subsets
LeetCode 1255.    Maximum Score Words Formed by Letters
LeetCode 301.     Remove Invalid Parentheses           -- advanced; pruning / BFS

## Time and Space Complexity

Backtracking complexity depends on the number of choices, recursion
depth, and the cost of checking or copying each solution.

-   **Time:** Often exponential or factorial, such as (O(2\^n)) for
    exploring subsets or (O(n!)) for generating permutations. These are
    common patterns, not universal bounds.
-   **Auxiliary space:** Often (O(d)), where (d) is the maximum
    recursion depth, excluding stored answers.
-   **Output space:** Can be large when the problem asks to store every
    solution. Include this separately when analysing space complexity.
-   **Pruning:** Can reduce the amount of work substantially, but does
    not always change the worst-case complexity.

## LeetCode 46 --- Permutations

**Problem:** Given an array of distinct integers, return all possible
permutations.

### Core idea

At each step, choose one number that has not been used yet. Add it to
the current permutation, recurse, and then undo the choice so another
number can be tried.

### Important state

-   `path`: the permutation being built.
-   `used`: tracks which numbers are already in `path`.
-   `result`: stores completed permutations.

### Checklist

-   [ ] Define the base case: when `len(path) == len(nums)`, save a copy
    of `path`.
-   [ ] Loop through the available numbers.
-   [ ] Skip numbers already used.
-   [ ] Choose a number and mark it as used.
-   [ ] Recurse.
-   [ ] Undo both the `path` update and the `used` update.

**Complexity:** There are (n!) permutations. Copying each permutation
takes (O(n)), so the total time is (O(n `\cdot `{=tex}n!)). Auxiliary
recursion/state space is (O(n)), excluding the output; storing all
permutations takes (O(n `\cdot `{=tex}n!)) space.

## Backtracking Checklist

Before coding, ask:

1.  What does one recursive call represent?
2.  What choices can I make at this step?
3.  What is the base case?
4.  How do I know a choice is invalid or unnecessary?
5.  What state must I update before recursion?
6.  What state must I restore afterward?
7.  Am I returning one answer or collecting all answers?
8.  Do I need to handle duplicate choices?

**Golden rule:** Make a choice → recurse → undo the choice.
