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
- [ ] 14.5
- [ ] 15.4, 15.9
- [ ] 16.5, 16.7
Greedy Algorithms and Invariants      
- [ ] 17.1 Compute optimum Assignment of Tasks
- [ ] 17.2 Schedule Optimum minimize waiting time
- [ ] 17.3 The interval covering problem
- [ ] 17.4 The 3-sum problem
- [ ] 17.7 Compute maximum water trapped by a pair of vertical lines
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
