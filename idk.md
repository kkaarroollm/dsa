# 📚 Abstract vs Concrete Data Structures

## ✅ Tabela: Abstract vs Concrete Structures

| **Abstract Data Structure** | **Possible Concrete Implementations**      | **Description**                                  |
|-----------------------------|---------------------------------------------|--------------------------------------------------|
| **Stack**                   | Array, Linked List                          | LIFO: push, pop, top                             |
| **Queue**                   | Array, Doubly Linked List                   | FIFO: enqueue, dequeue                           |
| **Deque**                   | Doubly Linked List                          | Double-ended queue                               |
| **Priority Queue**          | Binary Heap                                 | Remove element with highest (or lowest) priority |
| **Dictionary / Map**        | Hash Table, Binary Search Tree (BST)        | Key-value lookup                                 |
| **Set**                     | Hash Set, Balanced BST                      | Collection of unique elements                    |
| **Graph**                   | Adjacency List, Adjacency Matrix            | Nodes and edges                                  |
| **Tree**                    | Binary Tree, AVL Tree, Red-Black Tree       | Hierarchical structure                           |

---

## ⏱️ Tabela: Time Complexity of Common Structures

| **Structure**         | **Operation**          | **Avg. Time** | **Worst Case** | **Notes**                                       |
|-----------------------|------------------------|---------------|----------------|-------------------------------------------------|
| **Array (static)**    | access                 | O(1)          | O(1)           | Random access by index                          |
|                       | insert/delete          | O(n)          | O(n)           | Elements may need shifting                      |
| **Linked List**       | access                 | O(n)          | O(n)           | Sequential traversal                            |
|                       | insert/delete (head)   | O(1)          | O(1)           | Fast at the head                                |
| **Stack (array/list)**| push/pop               | O(1)          | O(1)           | LIFO behavior                                   |
| **Queue (list)**      | enqueue/dequeue        | O(1)          | O(1)           | FIFO behavior                                   |
| **Deque**             | insert/delete at ends  | O(1)          | O(1)           | Double-ended queue                              |
| **Hash Table**        | insert/search/delete   | O(1)          | O(n)           | Worst case: many collisions                     |
| **BST (unbalanced)**  | insert/search/delete   | O(log n)      | O(n)           | Depends on tree shape                           |
| **AVL / Red-Black Tree** | insert/search/delete| O(log n)      | O(log n)       | Self-balancing                                  |
| **Binary Heap (PQ)**  | insert                 | O(log n)      | O(log n)       | Maintains heap property                         |
|                       | extract-min/max        | O(log n)      | O(log n)       |                                                 |
| **Graph (adj. list)** | add edge               | O(1)          | O(1)           |                                                 |
|                       | search edge            | O(V)          | O(V)           | V = number of vertices                          |

---

## 🧠 Summary

- **Abstract structures** describe *what* operations are supported.
- **Concrete structures** define *how* these operations are implemented.
- Time complexity depends heavily on the chosen implementation.