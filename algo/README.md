- [Data Structures](#data-structures)
  - [Queue](#queue)
  - [Tree](#tree)
    - [Binary Tree](#binary-tree)
      - [Binary Search Tree (Sorted Binary Tree)](#binary-search-tree-sorted-binary-tree)
      - [Segment Tree](#segment-tree)
      - [Heap](#heap)
    - [Trie (Prefix Tree)](#trie-prefix-tree)
    - [Union-Find(Disjoint Set)](#union-finddisjoint-set)
  - [Graph](#graph)
    - [Kruskal algorithm](#kruskal-algorithm)
- [Algorithms](#algorithms)
  - [Dynamic Programming](#dynamic-programming)
  - [Divide \& Conquer](#divide--conquer)
  - [Greedy](#greedy)
  - [Search](#search)
    - [1) Exhausitive Search](#1-exhausitive-search)
    - [2) Breadth First Search](#2-breadth-first-search)
    - [3) Depth First Search](#3-depth-first-search)
    - [4) Binary Search](#4-binary-search)
    - [5) Backtracking](#5-backtracking)
  - [Sort](#sort)
    - [1) Normal](#1-normal)
    - [2) Counting sort](#2-counting-sort)
    - [3) Topological sort](#3-topological-sort)
  - [Shortest Path](#shortest-path)
    - [1) Dijkstra's algorithm](#1-dijkstras-algorithm)
    - [2) Floyd–Warshall algorithm](#2-floydwarshall-algorithm)
    - [3) Bellman–Ford algorithm](#3-bellmanford-algorithm)
  - [Advanced](#advanced)
    - [1) Two Pointers](#1-two-pointers)
    - [2) Prefix sum (구간 합)](#2-prefix-sum-구간-합)


# Data Structures

## Queue

**큐를 활용한 요세푸스 문제 (원배열에서 전부 제거될 때까지 K번째 제거)**
```python
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
```

## Tree
### Binary Tree

#### Binary Search Tree (Sorted Binary Tree)

#### Segment Tree
It is a type of binary tree, specifically designed for numerical data.

#### Heap

### Trie (Prefix Tree)

### Union-Find(Disjoint Set)
A collection of trees


## Graph
그래프를 표현하는 방법은 아래 두가지:

1. 인접행렬 : 정점의 개수가 적은 경우에만 사용하는 것을 권장. 왜냐하면, 정점n개에 대해 행렬의 크기가 n\*n만큼 차지하기 때문에 n의 수가 시간복잡도 O(V^2).
2. 인접리스트 : 모든 정점을 탐색하는 최악의 경우를 제외한 나머지 경우 인접행렬보다는 빠른 시간복잡도 O(V+E)

### Kruskal algorithm

# Algorithms
## Dynamic Programming
중복 계산되는 값을 이용하여 불필요한 계산을 줄이고 효율적으로 최적해 찾는 경우

## Divide & Conquer

## Greedy

부분적인 최적해가 모여서 결국 전체의 최적해가 되는 경우

## Search

### 1) Exhausitive Search
### 2) Breadth First Search
큐로 구현 가능. 주로 최단 경로 찾기에 많이 사용

### 3) Depth First Search
재귀나 스택으로 구현 가능. 이동한 정점에서 계속 이어서 탐색

### 4) Binary Search

### 5) Backtracking

## Sort

### 1) Normal

### 2) Counting sort

### 3) Topological sort

## Shortest Path

### 1) Dijkstra's algorithm
Time complexity : O(V + ElogV)  
한 지점에서 다른 특정 지점까지의 최단 경로 구함.

### 2) Floyd–Warshall algorithm
Time complexity : N\*O(N^2) (a.k.a. O(N^3))  
모든 지점에서 다른 모든 지점까지의 최단 경로 구함.

### 3) Bellman–Ford algorithm

Time complexity : O(V\*E)  
Dijkstra보다 구현이 간단하지만 더 느림

## Advanced

### 1) Two Pointers

### 2) Prefix sum (구간 합)
