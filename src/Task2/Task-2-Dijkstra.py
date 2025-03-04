
# ------------------------------------------------------------1------------------------------------------------------
# def find_start_end(matrix):
#     start, end = None, None
#
#
#     # Find nodes od graph
#     for i, j, _ in matrix:
#         if i not in [x[1] for x in matrix]:
#             start = i
#         if j not in [x[0] for x in matrix]:
#             end = j
#
#     return start, end
#
# import networkx as nx
#
# # example
# matrix = [[1, 17, 6], [1,13, 5], [1, 16, 6], [1, 12, 7], [1, 2, 2], [2, 11, 5], [2, 14, 1], [3, 6, 2],
#           [4, 19, 5], [5, 7, 5], [6, 14, 1], [7, 0, 4], [8, 0, 2], [9, 0, 2], [9, 19, 3],[10, 15, 5],
#           [11, 18, 8], [12, 19, 6], [12, 8, 3], [13, 3, 5], [13, 11, 8], [13, 15, 6], [13, 9, 2], [13, 4, 2],
#           [13, 5, 5], [14, 0, 10], [15, 19, 5],[16, 9, 6], [16, 10, 2], [17, 18, 1], [18, 0, 3], [19, 0, 2]]
#
# Graph = nx.DiGraph()
# Graph.add_weighted_edges_from(matrix) # create graph from matrix
# start, end = find_start_end(matrix) #  find start and end
#
# # algorithms usage
# try:
#     shortest_path = nx.bellman_ford_path(Graph, start, end)
#     length = nx.bellman_ford_path_length(Graph, start, end) # length of shortest path
#     print("Shortest Path", start, "---> ", end, ":")
#     print(shortest_path, "Length:", length)
# except nx.NetworkXNoPath:
#     print("there is no path", start, "--->", end)

#     -----------------------------------------------------2------------------------------------------------------
import numpy as np
def gtnel_skizb_verj(matrix):
    skizb, verj = None, None


    # Find the nodes
    for i, j, _ in matrix:
        if i not in [x[1] for x in matrix]:
            skizb = i
        if j not in [x[0] for x in matrix]:
            verj = j

    return skizb, verj

def func(heravorutyunneri_matrix, skizb, verj):

    anverjutyun = float('inf')
    heravorutyun = [anverjutyun] * gagatneri_qanak
    aycelvacner = [None] * gagatneri_qanak
    heravorutyun[skizb] = 0

    for _ in range(gagatneri_qanak - 1): # iteracianeri qanaky yst orenqi
        for i in range(gagatneri_qanak):
            for j in range(gagatneri_qanak):
                # matrixi mej for enq pttvum amen mi gagatic myus gagat heravorutyunnery hamematelu u amenakarchery gtnelu u pahelu hamar
                if heravorutyunneri_matrix[i][j] != 0  and heravorutyun[i] + heravorutyunneri_matrix[i][j] < heravorutyun[j]:
                    heravorutyun[j] = heravorutyun[i] + heravorutyunneri_matrix[i][j]
                    aycelvacner[j] = i

    chanaparh = []
    k = verj
    while k is not None:
        chanaparh.append(k)
        k = aycelvacner[k]
    chanaparh.reverse()

    return chanaparh, heravorutyun[verj]

# orinak
matrix = [[1, 2, 6], [1,3, 3],  [1, 4, 2], [1, 5, 8], [2, 6, 5], [2, 8, 9], [3, 6, 2],
          [3, 7, 8], [3, 8, 5],[4, 7, 4], [4, 8, 7],[5, 6, 5], [5, 7, 1], [5, 8, 6],
          [6, 10, 5],[6, 11, 9], [6, 12, 6], [6, 14, 8],[7, 9, 7], [7, 12, 1], [7, 13, 10],
          [8, 10, 3], [8, 11, 5],[8, 12, 2], [8,13, 3], [8, 14, 3],[9, 15, 5], [9, 16, 6],
          [10, 15, 4], [10,16, 3],[11, 15, 2], [11,17, 6],[12, 15, 8], [12, 16, 4],
          [13, 16, 8], [13,17, 9],[14, 16, 6], [14, 17, 2],[15, 18, 6], [15, 19, 2],
          [16, 18, 3], [16, 19, 1],[17, 18, 3], [17,19, 4],[18, 0, 5], [19, 0, 3]]

# kaperi- heravorutyunneri matrix
gagatner = set()
for lister in matrix:
    gagatner.add(lister[0])
    gagatner.add(lister[1])
gagatneri_qanak = len(gagatner)
heravorutyunneri_matrix = np.zeros((gagatneri_qanak, gagatneri_qanak), dtype=int) # 0 ner enq lcnum matrici mej
for lister in matrix:
    heravorutyunneri_matrix[lister[0]][lister[1]] = lister[2] # stanum enq matricy i-skizb, j-verj ev Aij = heravorutyuny i-ic j

# Main code
skizb, verj = gtnel_skizb_verj(matrix)
# talis enq skizby verjy u heravorutyunnern iraric, hashvum e amenakarch chanaparhy skzbic verj ev dra erkarutyuny
amenakarch_chanaparh, erkarutyun = func(heravorutyunneri_matrix, skizb, verj)

print("The shortest path of:", skizb, "--->", verj, ":")
print(amenakarch_chanaparh, "Shortest distance:", erkarutyun)

