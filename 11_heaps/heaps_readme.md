# Heaps

## What is a Heap?

A **heap** is a specialized tree-based data structure that satisfies the heap property:
- **Min Heap**: Parent node is smaller than or equal to its children
- **Max Heap**: Parent node is greater than or equal to its children

Heaps are commonly implemented as **binary heaps** using a list/array where:
- Parent of node at index `i` is at `i // 2`
- Left child of node at index `i` is at `2*i + 1`
- Right child of node at index `i` is at `2*i + 2`

**Key operations**: insert (O(log n)), delete/extract min/max (O(log n)), peek min/max (O(1))

## Python Implementation

Python provides the `heapq` module for min heaps:

```python
import heapq

# Create a min heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

# Extract minimum
min_val = heapq.heappop(heap)  # 1
print(min_val)

# Peek at minimum without removing
print(heap[0])  # 3

# Create heap from list
data = [9, 5, 6, 2, 3]
heapq.heapify(data)  # In-place: O(n)
print(data)  # [2, 3, 6, 5, 9]
```

For **max heap**, negate values:
```python
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
print(-heapq.heappop(max_heap))  # 5
```

## Common Use Cases

- Priority queues
- Heap sort
- Finding k smallest/largest elements
- Dijkstra's algorithm
- Huffman coding


## Problems (easy to hard)

Work top to bottom. Each level adds one new idea on top of the last.

### Level 1 - Use the heap as a priority queue
LeetCode 703.     Kth Largest Element in a Stream                 -- min-heap of size k
LeetCode 1046.    Last Stone Weight                               -- max-heap
LeetCode 215.     Kth Largest Element in an Array
LeetCode 973.     K Closest Points to Origin

### Level 2 - Top K and scheduling
LeetCode 347.     Top K Frequent Elements
LeetCode 451.     Sort Characters By Frequency
LeetCode 767.     Reorganize String                               -- always pick the most frequent
LeetCode 621.     Task Scheduler
LeetCode 378.     Kth Smallest Element in a Sorted Matrix

### Level 3 - Merge and multi-source
Idea: push the next element of whichever list you just popped from.

LeetCode 23.      Merge k Sorted Lists
LeetCode 264.     Ugly Number II
LeetCode 373.     Find K Pairs with Smallest Sums
LeetCode 355.     Design Twitter

### Level 4 - Hard (two heaps, greedy + heap)
LeetCode 295.     Find Median from Data Stream                    -- max-heap + min-heap
LeetCode 502.     IPO
LeetCode 1642.    Furthest Building You Can Reach
LeetCode 632.     Smallest Range Covering Elements from K Lists
