# Grading System
- This is my own grading system for myself how I assess my capability
to solve a problem

**EASY** = 0, I solved it without any help using optimum time complexity and space complexity. I am able to justify every step and different approaches

**MEDIUM** = 1, Solved but needed some clarification and took a long time to understand the problem.

**HARD** = 2, Needed help to solve and didn't solve on my own. Had to look up answer

**DIDNT_GET_QUESTION** = 3, Didn't understand the problem. Some of these problems are difficult to understand, so sometimes I end up looking at the answer and realize what they weren't asking. Hoping this wouldn't happen in a real interview because the interviewer would be able to ask these questions


WHITE_NINJA = 1
- Represents a problem in EPI, that given good enough time, a good
candidate should be able to solve

BLACK_NINJA = 2
- Represents a problem in EPI, that the interviewer isn't expecting the
best and most perfect solution, but more of a stress test
# TODO
- [ ] 4.3, 4.11
- [ ] 5.5, 5,9
- [ ] 6.7, 6.8
- [ ] 7.10
- [ ] 8.3, 8.8
- [ ] 9.11
**Heaps** 4/6
- [ EASY ] 10.4 Compute the k closest stars: 4/6
- [ EASY ] 10.5 Compute the median of online data: 4/6
**Searching**
- [ ] 11.5, 11.10
**Hash Tables**
- [ ] 12.4, 12,6
- [ ] 13.8, 13.11
- **BST Problems** 4/6
- [ MEDIUM ] 14.4 Least Common Ancestor 4/1 - I got it, but probably wouldn't have
been able to fully justify in an interview setting
- [ MEDIUM ] 14.5, BST from pre order. very similar to 24.21
- [ MEDIUM ] 24.21, Sorted List to BST very similar to 14.5
- [ HARD ] Inorder Traversal of a BST without recursion
- [ ] 15.4, 15.9
- [ ] 16.5, 16.7
- **Greedy Algorithms and Invariants** 4/31    
- [ EASY ] 17.1 Compute Optimum Assignment of Tasks
- [ DIDNT_GET_QUESTION ] 17.2 Schedule Optimum minimize waiting time
- [ MEDIUM ] 17.3 The interval covering problem
- [ MEDIUM ] 17.4 The 3-sum problem
- [ ] 17.7 Compute maximum water trapped by a pair of vertical lines
- [ MEDIUM ] Trapping water 24.32
- [ ] 18.3
- [ ] 19.9
- [ ] 20.1
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
