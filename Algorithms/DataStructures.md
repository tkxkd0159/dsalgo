# Tips related to simple DSs

## Queue

### 1) 큐를 활용한 요세푸스 문제 (원배열에서 전부 제거될 때까지 K번째 제거)

```python
while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
```

## Graph

그래프를 표현하는 방법은 아래 두가지:

1. 인접행렬 : 정점의 개수가 적은 경우에만 사용하는 것을 권장. 왜냐하면, 정점n개에 대해 행렬의 크기가 n\*n만큼 차지하기 때문에 n의 수가 시간복잡도 O(V^2).
2. 인접리스트 : 모든 정점을 탐색하는 최악의 경우를 제외한 나머지 경우 인접행렬보다는 빠른 시간복잡도 O(V+E)

### 1) Trie

### 2) Heap

연산하면서 다시 넣고 뺄 때 정렬을 유지해야할 필요가 있으면 heap 사용 고려

### 3) Union-Find(Disjoint set)

### 4) Kruskal algorithm

### 5) Segment tree

lazy propagation
