# Dynamic Programming

중복 계산되는 값을 이용하여 불필요한 계산을 줄이고 효율적으로 최적해 찾는 경우

# Divide & Conquer

# Greedy

부분적인 최적해가 모여서 결국 전체의 최적해가 되는 경우

# Search

## 1) Exhausitive Search

## 2) Breadth First Search

큐로 구현 가능. 주로 최단 경로 찾기에 많이 사용

## 3) Depth First Search

재귀나 스택으로 구현 가능. 이동한 정점에서 계속 이어서 탐색

## 4) Binary Search

## 5) Backtracking

# Sort

## 1) Normal

## 2) Counting sort

## 3) Topological sort

# Shortest Path

## 1) Dijkstra's algorithm

Time complexity : O(V + ElogV)  
한 지점에서 다른 특정 지점까지의 최단 경로 구함.

## 2) Floyd–Warshall algorithm

Time complexity : N\*O(N^2) (a.k.a. O(N^3))  
모든 지점에서 다른 모든 지점까지의 최단 경로 구함.

## 3) Bellman–Ford algorithm

Time complexity : O(V\*E)  
Dijkstra보다 구현이 간단하지만 더 느림

# Advanced

## 1) Two Pointers

## 2) Prefix sum (구간 합)
