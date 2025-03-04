# **Graph Analysis using Information Flow Method**

## **Exercise 2: Finding the Shortest Path in a Directed Graph**

### **Introduction**
The second problem in this course project focuses on developing an algorithm and a program to find the shortest path from the initial vertex to the final vertex in a directed graph. The graph consists of vertices and edges, where the edges represent distances or weights between nodes.

The goal is to determine the shortest distance from the input node to the output node and identify the optimal route using an **iterative computation method**.

Shortest path algorithms focus on finding the minimum-length path from the initial vertex to the final vertex while optimizing time and space complexity.

For solving this problem, we will use an iterative method, while also considering:
- **Dijkstra's Algorithm** (optimal for non-negative weights, with time complexity `O((V + E) log V)`)
- **Bellman-Ford Algorithm** (handles negative weights but is less efficient, with time complexity `O(V * E)`)
- **Breadth-First Search (BFS)** (used for unweighted graphs with time complexity `O(V + E)`)

### **Comparison of Algorithms**
- **Dijkstra’s Algorithm** is the best choice for non-negative weighted graphs.
- **Bellman-Ford Algorithm** can handle negative weights but is slower.
- **BFS** is useful when edge weights do not play a significant role.

Among these, **Dijkstra’s Algorithm** is the most commonly used and is considered the most optimal solution for similar problems.

### **Objectives**
- Determine the shortest path from the start node to the end node.
- Use an iterative method to solve the problem efficiently.
- Analyze different shortest path algorithms and select the most optimal one.
- Implement the algorithm using a programming language.
- Provide a conclusion based on the results.

### **Graph Representation**
![my_graph2.png](../images/my_graph2.png)
---

## **Usage**
To be determined based on the final implementation, but it will likely involve providing a graph input and receiving analysis results as output.

