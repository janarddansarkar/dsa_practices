# Prefix Sum Algorithm

## What is Prefix Sum?

A prefix sum (cumulative sum) is an array where each element at index `i` contains the sum of all elements from index `0` to `i` (inclusive) from the original array. It allows you to calculate the sum of any subarray in **O(1)** time after **O(n)** preprocessing.

**Formula:** `prefix[i] = prefix[i-1] + arr[i]`

## Common Patterns

1. **Range Sum Queries** - Get sum of elements between indices `i` and `j` in O(1) time
   - Query: `sum(i, j) = prefix[j] - prefix[i-1]`

2. **2D Prefix Sum** - Extend prefix sum to 2D matrices for rectangle sum queries

3. **Difference Array** - Efficient range updates (opposite of prefix sum)

4. **Cumulative Frequency** - Track running totals for statistics

## Examples

### Example 1: Range Sum Query
```python
# Original array
arr = [1, 2, 3, 4, 5]

# Build prefix sum
prefix = [0, 1, 3, 6, 10, 15]
# prefix[0] = 0
# prefix[1] = 1
# prefix[2] = 1+2 = 3
# prefix[3] = 1+2+3 = 6
# prefix[4] = 1+2+3+4 = 10
# prefix[5] = 1+2+3+4+5 = 15

# Query: sum from index 1 to 3 (elements 2,3,4)
sum(1, 3) = prefix[3] - prefix[0] = 6 - 0 = 6 ✓ (2+3+4=9... wait)
# Corrected: sum(1, 3) = prefix[4] - prefix[1] = 10 - 1 = 9 ✓
```

### Example 2: Count Subarray Sum Equals K
```python
# Problem: Count subarrays with sum = 5
arr = [1, 2, 1, 2, 1, 5]

# Using prefix sum + hashmap
# If prefix[j] - prefix[i] = k, then sum(i+1, j) = k
# We track prefix sums we've seen and count matches

count = 0
prefix_sum = 0
sum_map = {0: 1}  # Initialize with 0 having count 1

for num in arr:
    prefix_sum += num
    target = prefix_sum - 5
    if target in sum_map:
        count += sum_map[target]
    sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1

# Result: count = 2 (subarray [5] and [2,1,2])
```


## Problems (easy to hard)

Work top to bottom. Each level adds one new idea on top of the last.

### Level 1 - Build and query a prefix array
LeetCode 1480.    Running Sum of 1d Array  - DONE
LeetCode 303.     Range Sum Query - Immutable  - DONE
LeetCode 724.     Find Pivot Index                                -- left sum == total - left - x - DONE

### Level 2 - Prefix sum + hash map
Idea: if prefix[j] - prefix[i] = k then sum(i+1..j) = k.

LeetCode 560.     Subarray Sum Equals K  - DONE
LeetCode 525.     Contiguous Array                                -- treat 0 as -1 - DONE
LeetCode 523.     Continuous Subarray Sum                         -- store prefix % k - DONE
LeetCode 974.     Subarray Sums Divisible by K

### Level 3 - 2D prefix sum
LeetCode 304.     Range Sum Query 2D - Immutable  - DONE
LeetCode 1314.    Matrix Block Sum  - DONE

### Level 4 - Prefix product and difference array
Idea: difference array = range updates in O(1), then one prefix pass.

LeetCode 238.     Product of Array Except Self                    -- prefix product x suffix product
LeetCode 1109.    Corporate Flight Bookings                       -- difference array
LeetCode 1094.    Car Pooling                                     -- difference array
LeetCode 437.     Path Sum III                                    -- prefix sum on a tree path
