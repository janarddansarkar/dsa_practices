# Greedy Algorithm

> ⚠️ A greedy algorithm does **not** guarantee the optimal solution for every problem.

## What is a Greedy Algorithm?

A **greedy algorithm** always makes the best possible choice at the current moment, hoping that these local optimal choices will eventually lead to the overall optimal solution.

Think of it like this:

> **"I won't worry about the future. I'll simply choose the best option available right now."**

Once a decision is made, a greedy algorithm **never goes back** to change it.

---

## Example

Suppose you need to make **₹93** using the following denominations:

- ₹50
- ₹20
- ₹10
- ₹5
- ₹2
- ₹1

### Greedy Approach

At each step, choose the **largest denomination** that does not exceed the remaining amount.

| Step | Chosen Note/Coin | Remaining Amount |
|------|------------------:|-----------------:|
| 1 | ₹50 | ₹43 |
| 2 | ₹20 | ₹23 |
| 3 | ₹20 | ₹3 |
| 4 | ₹2 | ₹1 |
| 5 | ₹1 | ₹0 |

So, the selected denominations are:

```
50 → 20 → 20 → 2 → 1
```

---

## How a Greedy Algorithm Thinks

For every decision, it asks:

1. Which option looks **best right now**?
2. Choose that option.
3. Move forward.
4. Never reconsider previous choices.

In short:

> **Choose the best now, hope it's best overall.**


## Problems (easy to hard)

Work top to bottom. Each level adds one new idea on top of the last.

### Level 1 - Obvious local choice
LeetCode 455.     Assign Cookies                                  -- sort both, match smallest - DONE
LeetCode 860.     Lemonade Change                                 -- keep the bigger notes for later - DONE
LeetCode 122.     Best Time to Buy and Sell Stock II
LeetCode 976.     Largest Perimeter Triangle

### Level 2 - Sort, then sweep
LeetCode 55.      Jump Game                                       -- track farthest reach
LeetCode 45.      Jump Game II
LeetCode 134.     Gas Station
LeetCode 135.     Candy                                           -- two passes
LeetCode 763.     Partition Labels

### Level 3 - Intervals
Idea: sort by END time to keep the most intervals.

LeetCode 435.     Non-overlapping Intervals
LeetCode 452.     Minimum Number of Arrows to Burst Balloons
LeetCode 56.      Merge Intervals
LeetCode 1094.    Car Pooling

### Level 4 - Harder greedy
LeetCode 621.     Task Scheduler
LeetCode 767.     Reorganize String
LeetCode 406.     Queue Reconstruction by Height
LeetCode 678.     Valid Parenthesis String                        -- track a range of open counts
LeetCode 402.     Remove K Digits
LeetCode 316.     Remove Duplicate Letters

### Level 5 - Hard
LeetCode 330.     Patching Array
