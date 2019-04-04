# Grading System
- This is my own grading system for myself how I assess my capability
to solve a problem

**EASY** = 0, I solved it without any help using optimum time complexity and space complexity. I am able to justify every step and different approaches

**MEDIUM** = 1, Solved but needed some clarification and took a long time to understand the problem.

**HARD** = 2, Needed help to solve and didn't solve on my own. Had to look up answer

**DIDNT_GET_QUESTION** = 3, Didn't understand the problem. Some of these problems are difficult to understand, so sometimes I end up looking at the answer and realize what they weren't asking. Hoping this wouldn't happen in a real interview because the interviewer would be able to ask these questions

# TODO
- [ ] 4.3, 4.11
- [ ] 5.5, 5,9
- [ ] 6.7, 6.8
- [ ] 7.10
- [ ] 8.3, 8.8
- [ ] 9.11
- [ ] 10.5
- [ ] 11.5, 11.10
- [ ] 12.4, 12,6
- [ ] 13.8, 13.11
- **BST Problems**
- [ MEDIUM ] 14.4 Least Common Ancestor 5/1 - I got it, but probably wouldn't have
been able to fully justify in an interview setting
- [ DIDNT_GET_QUESTION ] 14.5, BST from pre order. very similar to 24.21
- [ DIDNT_GET_QUESTION ] 24.21, Sorted List to BST very similar to 14.5

- [ ] 15.4, 15.9
- [ ] 16.5, 16.7
- **Greedy Algorithms and Invariants** 4/31    
- [ EASY ] 17.1 Compute Optimum Assignment of Tasks
- [ DIDNT_GET_QUESTION ] 17.2 Schedule Optimum minimize waiting time
- [ MEDIUM ] 17.3 The interval covering prls
oblem
- [ MEDIUM ] 17.4 The 3-sum problem
- [ ] 17.7 Compute maximum water trapped by a pair of vertical lines
- [ ] Trapping water 24.32
- [ ] 18.3
- [ ] 19.9
- [ ] 20.1
Completed - Review on a weekly basis
14.8
Needs Work
- bst_from_preorder 3/24
- bst_from_sorted_array 3/24

Tool Tips for Data Structures

# Graphs
- It's natural to use a graph when the problem involves spatially connected objects
e.g. roads/segments between cities
- More generally, consider using a graph when you need to analyze any binary
relationship between 2 objects, such as interlinked webpages, followers in a
social graph, etc. In such cases, quite often the problem can be reduced to
a well-known graph problem
- Some graph problems are related to *optimization*, e.g. find the shortest
path from one to another. BFS, Djikstra's shortest path algorithm and minimum
spanning trees of graph algorithms that are appropriate for optimization problems

## Graph Problems
- fill_surrounded_regions

# Greedy Algorithms and Invariants Ch 17
- A greedy algorithm is often the right choice for an *optimization problem* where there is a natural set of *choices to select from*
- It's often easier to conceptualize a greedy algorithm recursively, and then implement it using iteration for higher performance
- Even if the greedy approach does not yield an optimum solution, it can give insights into the optimum algorithm, or serve as a heuristic.
- Sometimes the correct greedy algorithm is *not obvious*

# Invariants
- Key strategy to determining whether to use an invariant and when designing an algorithm is to work on small examples to hypothesize the invariant

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
then the student's GPA needs to be updated, all we have is the student's name and
new GPA, we cannot find the student by name without full traversal. However, with
an additional hash table, we can directly go to the corresponding entry in the tree

##
