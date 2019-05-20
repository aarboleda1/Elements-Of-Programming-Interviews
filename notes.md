# Total Count Solved: 7

# HISTORY LOG
*5/20*
- [ ATTEMPTED ] find_smallest_sequentially_covering_subset
- []
- []
- []
*5/19*
- [ ATTEMPTED ] Getting different number https://www.pramp.com/challenge/aK6V5GVZ9MSPqvG1vwQp
- [ ATTEMPTED ] 5.12 Sample offline data/offline_sampling.py
- [ ATTEMPTED ] 5.18 Compute the spiral ordering of a 2D array/matrix_in_spiral_order.py
- [ ATTEMPTED ] 5.17 The Sudoku Checker Problem
- [ SOLVED ] 5.1 The Dutch National Flag Problem
  - do again to confirm logic

*5/18* HashTable Bootcamp/KB/BST_TO_DLL
- [ ATTEMPTED ] Interview with KB - https://leetcode.com/problems/design-log-storage-system/
- [ ATTEMPTED ] find_smallest_sequentially_covering_subset.py
- [ SOLVED ] - 24.21 bst_to_doubly_linked_list
- [ SOLVED ] 12.1 Test for palindromic permutations, is_string_permutable_to_palindrome.py
- 12.2 [ REDO, SOLVED ] Is an anonymous letter constructible, is_letter_constructible.py
  - Optimize for solving with the letter_text rather than magazine_text
- 12.3 [ ATTEMPTED ] Implement an ISBN cache
- 12.5 [ SOLVED ] Find the nearest repeated entries in an array

*5/17*
  - [ ATTEMPTED ] find_smallest_subarray_covering_set.py
  - [ ATTEMPTED ] find_smallest_sequentially_covering_subset.py
  - [ SOLVED ] bst_iterator.py

*5/16*  
  - [ ATTEMPTED ] 24.21 BST to Doubly-Linked List
  - [ ATTEMPTED ] sorted_list_to_bst
  - [ SOLVED ] 24.22 bst_merge, do above problems, and this problem becomes very
    trivial
  - [ SOLVED ] 12.5 Find the nearest repeated entries in an array

*5/15*:
  - [ SOLVED ] 12.6 find_smallest_subarray_covering_set.py
*5/14*:
- [ ATTEMPTED ] 24.21 BST to Doubly-Linked List:
REDO AND WHITEBOARD, answer is still not clear
- [ ATTEMPTED ] 24.22 bst_merge
- [ ATTEMPTED ] 12.6 find_smallest_subarray_covering_set.py

- [ SOLVED ] power_set, "Generate powersets"
- [ SOLVED ] 14.1 is_tree_a_bst.py "Given a Binary Tree determine if it is a BST"
- [ SOLVED ] bst_from_preorder_sequence "Generate BST from preorder_sequence"
- [ SOLVED ] sorted list to BST "Given a sorted list, generate a BST"
*5/13*: power_set
*5/11* Design Twitter

# TODO
- [ ] 4.3, 4.11
- [ ] 5.5, 5,9
- [ ] 6.7, 6.8
- [ ] 7.10
- [ ] 8.3, 8.8
- [ ] 9.11

**Arrays** 5/19
- [ ATTEMPTED ] 5.12 Sample Offline Data
- [ ATTEMPTED ] 5.18 Compute the spiral ordering of a 2D array
- [ SOLVED ] 5.1 The Dutch National Flag Problem
  - Should probably do this one again though as I wasn't as
  convincing in the walk through
- [ SOLVED ] 5.6 Buy and Sell a stock once
- [ ] 5.17 The Sudoku Checker Problem
- [ ] 5.5
- [ ] 5.9

**Heaps** 4/6
- [ EASY ] 10.4 Compute the k closest stars:
  - 4/6
- [ EASY ] 10.5 Compute the median of online data: 4/6

**Searching**
- [ ] 11.5, 11.10

**Sorting**
- [ EASY ] 13.1 intersect_sorted_arrays: 4/20

**Hash Tables** 5/14, 5/18
- 12.1 Test for palindromic permutations
  - [ SOLVED ] 5/18  
- 12.2 Is an anonymous letter constructible
  - [ SOLVED ] 5/18
- 12.3 Implement an ISBN cache
  - [ SOLVED ] 5/18
- 12.6 find_smallest_subarray_covering_set.py
  - [ ATTEMPTED ]  5/14
  - [ SOLVED ] - 5/15
- [ ] 12.4,
- [ ] 13.8
- [ ] 13.11

**BST Problems** 4/6, 5/14
- [ ATTEMPTED ] 14.4 Least Common Ancestor *4/1*
- [ ATTEMPTED ] 24.21, Sorted List to BST very similar to 14.5, *4/1*
- [ ATTEMPTED ] Inorder Traversal of a BST without recursion *4/1*
- [ SOLVED ] 24.21 BST to Doubly-Linked List *5/18*, *5/1*, *4/1*,
- [ SOLVED ] Sorted list to BST *5/14*
- [ SOLVED ] 14.5, BST from pre-order sequence. very similar to 24.21 *5/14*
- [ SOLVED ] 24.22 Merge BST  *5/14*
- [ SOLVED ] 14.1 Determine if a tree is a BST *5/14*

**Recursion**
Go over time complexity of these
- [ HARD ] 15.4 PowerSet
    - 5/7, Make sure to go over this problem using the iterative
      version
- [ HARD ] 15.5 Generate all subsets of size k,
    - 5/8, Still need to understand the recursion aspect
- [ ] 16.5, 16.7

**Greedy Algorithms and Invariants** 3/31    
- [ EASY ] 17.1 Compute Optimum Assignment of Tasks
- [ DIDNT_GET_QUESTION ] 17.2 Schedule Optimum minimize waiting time
- [ MEDIUM ] 17.3 The interval covering problem
- [ MEDIUM ] 17.4 The 3-sum problem
- [ ] 17.7 Compute maximum water trapped by a pair of vertical lines
- [ MEDIUM ] Trapping water 24.32
- [ ] 18.3
- [ ] 19.9
- [ ] 20.1

**Strings**
- [ MEDIUM ] 24.1 left_right_justify_test.py, JustifyText 4/18
Completed - Review on a weekly basis
14.8



## Tool Tips for Data Structures
# Arrays
**Tips**
- Filling an array from the front is slow, see if it's possible to *write
values from the back*
- Instead of deleting an entry, consider *overwriting* it.
- It's incredibly easy to make *off-by-1* errors when operating on arrays
reading past the last element of an array is a common error. Make sure
to always carefully walk thru example when working with arrays
**Know Array Libraries**
- What is the difference between copy.deepcopy(A) and copy.copy(A)? Read this article to see the differences.
https://realpython.com/copying-python-objects/

# Hash Tables
- **Hash Table Libraries**
  -  *Set*: Stores keys only. Unlike other libraries such as Collection and Counter
  library which stores key and the value. Main methods are s.add(), s.remove(),
  s.discard()
  - *Counter*: Used for counting the number of occurrences of keys, within
  a number of set-like operations
  `````
  c = collections.Counter(a=3, b=2)
  b = collections.Counter(a=1, b=0)

  c + b = Counter({'a': 4, 'b': 2})
  c - d = Counter({'a': 2, 'b': 2})
  # intersection: min(c[x], d[x]), Counter({'a': 2, 'b': 0})
  c & d
  # union: max(c[x], d[x]), Counter({'a': 3, 'b': 2})
  c | d
  `````  
  - *DefaultDict*: Returns the default value of the type that was specified
  when the collection was instantiated, e.g., if `d = defaultdict(list)`, then
  `if k not in d` then d[k] is []

# Graphs
- It's natural to use a graph when the problem involves spatially connected
objects e.g. roads/segments between cities
- More generally, consider using a graph when you need to analyze any binary
relationship between 2 objects, such as interlinked webpages, followers in a
social graph, etc. In such cases, quite often the problem can be reduced to
a well-known graph problem
- Some graph problems are related to *optimization*, e.g. find the shortest
path from one to another. BFS, Djikstra's shortest path algorithm and minimum
spanning trees of graph algorithms that are appropriate for optimization
problems

## Graph Problems
- fill_surrounded_regions

# Greedy Algorithms and Invariants Ch 17
- A greedy algorithm is often the right choice for an *optimization problem*
where there is a natural set of *choices to select from*
- It's often easier to conceptualize a greedy algorithm recursively, and then
implement it using iteration for higher performance
- Even if the greedy approach does not yield an optimum solution, it can give
insights into the optimum algorithm, or serve as a heuristic.
- Sometimes the correct greedy algorithm is *not obvious*

**Coin Change**
This is a classic greedy algorithm, where in coins take values 1,5,10,25,50,100
for US currencies. The greedy algorithm for making change results in the minimum
number of coins of a particular value, *it never changes that selection*. This
is the hallmark of a greedy algorithm

- Time complexity for this problem is O(1), because we will only perform 6
iterations and will not increase with the size of the input

```
def change_making(cents):
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in coins:
        num_coins += (coin // cents)
        cents %= coin
    return num_coins
```    

# Invariants
- Key strategy to determining whether to use an invariant and when designing
an algorithm is to work on small examples to hypothesize the invariant

# Binary Trees
- PreOrder: Node, left subtree, right subtree
- InOrder: left subtree, Node, right subtree
- PostOrder: left subtree, right subtree, Node

# BST
- Offer ability to efficiently search for a key, find min **AND** max elements,
look for the successor or predecessor of a search key, and enumerate keys in a
a range in sorted order, due to the BST properties

- With a BST, you can iterate thru elements in **sorted order** in time O(n)
regardless of whether it is balanced

- Some problems need a combination of a **BST and Hash Table**. For example if
you insert student objects into a BST and entries are ordered by GPA, and
then the student's GPA needs to be updated, all we have is the student's name
and new GPA, we cannot find the student by name without full traversal. However,
with an additional hash table, we can directly go to the corresponding entry
in the tree

## Tries
- Efficient for string searches

**Disadvantages of a Trie**
The main disadvantage of tries is that they need lot of memory for storing
the strings. For each node we have too many node pointers(equal to number of
characters of the alphabet), If space is concern, then Ternary Search Tree
can be preferred for dictionary implementations. In Ternary Search Tree,
time complexity of search operation is O(h) where h is height of the tree.
Ternary Search Trees also supports other operations supported by Trie like
prefix search, alphabetical order printing and nearest neighbor search.

The final conclusion is regarding tries data structure is that they are faster
but require huge memory for storing the strings.

## Primitive Types
- Be very comfortable with bitwise operators, particularly XOR
- Gayle McDowell: https://www.youtube.com/watch?v=NLKQEOgBAnw
Bitwise Operators
https://code.tutsplus.com/articles/understanding-bitwise-operators--active-11301

Signed bit, if first digit is a 0, it's a positive number. If first number is a 1, then it is a negative number

# Signedness
- Signedness of a data type indicates whether or not a variable of that type
can be a negative number. Specifically, if a numeric value is "unsigned", it
can only represent only a positive number of zero
- If a numeric variable is "signed," it can also represent a negative number
because one of the bits of data is dedicated to representing "positive" or
"negative".

# Recursion 4/24 REDO
- I did generate all subsets of of size k 15.5 and 15.4 generate the powerset,
both were pretty difficult for me. Where I got lost was determining with confidence
which subsets to generate


# Grading System
- This is my own grading system for myself how I assess my capability
to solve a problem

**EASY** = 0, I solved it without any help using optimum time complexity and space complexity. I am able to justify every step and different approaches

**MEDIUM** = 1, Solved but needed some clarification and took a long time to understand the problem.

**HARD** = 2, Needed help to solve and didn't solve on my own. Had to look up answer

**DIDNT_GET_QUESTION** = 3, Didn't understand the problem. Some of these problems are difficult to understand, so sometimes I end up looking at the answer and realize what they weren't asking. Hoping this wouldn't happen in a real interview because the interviewer would be able to ask these questions

## NINJA GRADING (The problems in the back of the book)
**WHITE_NINJA** = 1
- Represents a problem in EPI, that given good enough time, a good
candidate should be able to solve

**BLACK_NINJA** = 2
- Represents a problem in EPI, that the interviewer isn't expecting the
best and most perfect solution, but more of a stress test
