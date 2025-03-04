import numpy as np

# my graph:
graph = [[1, 17], [1, 16], [1, 12], [1, 2], [2, 11], [2, 14], [3, 6], [4, 19], [5, 7], [6, 14], [7, 0], [8, 0], [9, 0], [9,19],
          [10, 15], [11, 18], [12, 19], [12, 8], [13, 3], [13, 11], [13, 15], [13, 9], [13, 4], [13, 5], [14, 0], [15, 19],
          [16, 9], [16, 10], [17, 18], [18, 0], [19, 0]]
def analyze_of_graph(graph):
    t_1 = []
    t_2 = []
    t_3 = []
    t_5 = []
    t_6 = []
    for couple in graph:
        i, j = couple
        if i not in [x[1] for x in graph] and i not in t_1:
            t_1.append(i)
        elif i in [x[1] for x in graph] and j != 0 and i not in t_2:
            t_2.append(i)
        elif j == 0 and i not in t_3:
            t_3.append(i)
    for couple in graph:
        i, j = couple
        if i in t_2 and j in t_2:
            t_5.append(couple)
        elif i in t_3 and j!=0 and j not in [x[0] for x in t_6]:
            t_6.append(couple)

    t_1_count = len(t_1)
    t_2_count = len(t_2)
    t_3_count = len(t_3)
    t_5_count = len(t_5)
    t_6_count = len(t_6)
    m = max(max(couple) for couple in graph)
    km = t_2_count / m
    print("t1_count:", t_1_count)
    print("t1_list:", t_1)
    print("t2_count:", t_2_count)
    print("t2_list:", t_2)
    print("t3_count:", t_3_count)
    print("t3_list:", t_3)
    print("t5_count:", t_5_count)
    print("t5_list:", t_5)
    print("t6_count:", t_6_count)
    print("t6_list:", t_6)
    print("km:", km)
    return t_1, t_2, t_3, t_5, t_6, km

def neighborhood_matrix(graph):
    max_element = max(max(couple) for couple in graph)  # We find the maximum element of the graph in order to create our matrix
    size = max_element  # neighbor matrix size
    A = [[0] * size for _ in range(size)]  # matrix with 0 elements in order to fill then

    for couple in graph:
        i, j = couple
        if j != 0:  # ignore j=0 couples
            A[i - 1][j - 1] = 1

    return A

def formally_disconnected_elements(graph):
    disconnected_columns = [all(row[i] == 0 for row in graph) for i in range(len(graph[0]))]
    t_4_count = sum(disconnected_columns)
    t_4_list = [i + 1 for i, disconnected in enumerate(disconnected_columns) if disconnected]
    return t_4_count, t_4_list

t_1, t_2, t_3,t_5,t_6, km = analyze_of_graph(graph)
adjacency_graph = neighborhood_matrix(graph)
current_power = 1
delta = np.zeros_like(adjacency_graph)
kmo_sum = 0

while True:
    A_power = np.linalg.matrix_power(adjacency_graph, current_power)
    delta += A_power

    if np.any(np.diag(A_power) != 0): # has cycle or not
        print(f"graph has {current_power} length cycle.")
        break

    t_4_count, t_4_list = formally_disconnected_elements(A_power)
    t_7_count = t_4_count - current_power
    kmo = t_7_count /t_4_count
    kmo_sum += kmo
    print('\n')
    print(f"A neighbor matrix^{current_power}.")
    for row in A_power:
        print(row)
    print("t4_count:", t_4_count)
    print("t4_list:", t_4_list)
    print("t7_count:", t_7_count)
    print("kmo:", kmo)

    if np.all(A_power == 0):
        break
    current_power += 1
N = current_power  # save N without substructing 1
system_order = N - 1

print("System order or the longest way:", system_order)
print('\n')
print("Delta.")
for row in delta:
    print(row)
k = 2* len(t_6) / len(t_3)*(len(t_3)-1)
kmo_avg = kmo_sum /N
print('k։', k)
print("km:", km)
print("kmo average:", kmo_avg)
if abs(km-kmo_avg)<=0.01:
    print('The process of document circulation in the system is organized in a rational way.')
else:
    print('The process of document circulation in the system is organized in a not rational way.')
print('The end of project.')



