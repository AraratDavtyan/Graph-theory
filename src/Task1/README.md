# **Graph Analysis using Information Flow Method**

## **Introduction**
A graph consists of two sets: one representing vertices and the other representing edges. The set of edges defines the interconnection rules between vertices or, in other words, the mapping relationships between them.

A graph is called directed if the connections between vertices have a unidirectional flow. In this analysis, vertices represent documents, while edges denote information flows.

Analyzing a system using the information flow method involves:
- Determining the number and sets of input, intermediate, and output elements.
- Identifying the number of information paths of different lengths between these elements by constructing adjacency matrices of various degrees.
- Calculating specific coefficients whose numerical values help assess the system's complexity, internal connectivity, rational efficiency, and the degree of excess output information.

For analysis, the initial data is represented as a direct flow matrix `||Cij||`, where each element indicates direct information flow between two vertices.

From this matrix, we derive the adjacency matrix `A` of step `0`, excluding vertex `0`. It is called a step `0` matrix because the columns corresponding to input elements contain only zeros.

While constructing the adjacency matrix `A`, we consider:
- Direct flows between two vertices or unit-length connections.
- A value of `1` at the intersection of the corresponding row and column in the matrix.

After that, we generate the matrix `A^n`, whose elements indicate the number of paths of length `n` in the graph. The exponentiation continues until all elements become `0`. If `A^n = 0` (all elements are zeros), it implies that there are no paths of length `n`, and the longest path has a length of `n-1`, which is called the system’s order.

Once all matrices are obtained, we compute the accessibility matrix, which represents the sum of all matrices. Its elements indicate the number of all possible different paths between two vertices.

If any adjacency matrix has at least one `1` on its diagonal, it indicates the presence of a cycle in the system, and further computations are terminated.

## **Objectives**
- Identify the input, intermediate, and output elements of the graph, along with internal connections and unit connections between output elements.
- Generate the accessibility matrix of the graph.
- Identify formally disconnected elements and determine the number of elements formed sequentially in steps.
- Compute different degrees of neighborhood matrices, where elements represent the number of paths of varying lengths between vertices.
- Calculate coefficients to numerically evaluate the control system indicators:
  - Complexity degree (`km`)
  - Rationality (`|km - kmo_avg|`)
  - Redundancy degree between output elements (`k`)
- Develop the analysis algorithm and implement it in a programming language.
- Provide a conclusion based on the analysis.

## **Implementation Details**
- The project will be implemented using a suitable programming language.
- The algorithm will efficiently compute graph properties and perform the required calculations.
- The longest path in the graph will be determined automatically.

## **Expected Outcomes**
- A software tool capable of analyzing directed graphs representing document circulation.
- A comprehensive evaluation of the system’s complexity, rationality, and redundancy.
- Insights into the structure and efficiency of the document circulation scheme.

## **Graph Representation**
![my-graph1.png](../images/my-graph1.png)
## **Usage**
To be determined based on the final implementation, but it will likely involve providing a graph input and receiving analysis results as output.
