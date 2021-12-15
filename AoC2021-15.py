from collections import defaultdict
import bisect
import numpy as np

def process_input(file_path):
    f = open(file_path)
    lines = f.readlines()
    f.close()

    proto_arr = []
    for line in lines:
        row = [int(s) for s in line.strip()]
        proto_arr.append(row)
    proto_arr = np.array(proto_arr, dtype=int)

    (dx, dy) = proto_arr.shape
    arr = np.zeros((5 * dx, 5 * dy), dtype=int)
    for i in range(5):
        for j in range(5):
            arr[i*dx:(i+1)*dx, j*dy:(j+1)*dy] = (proto_arr - 1 + i + j) % 9 + 1;

    return arr

def neighbors(node, N, M):
    (i,j) = node
    nbs = []
    if (i + 1) < N:
        nbs.append((i+1, j))
    if (i - 1) >= 0:
        nbs.append((i-1, j))
    if (j + 1) < M:
        nbs.append((i, j+1))
    if (j - 1) >= 0:
        nbs.append((i, j-1))
    return nbs

def dijkstra(start, end, arr, N, M):
    MAX_VAL = 999999999999
    distances = defaultdict(lambda: MAX_VAL)
    distances[start] = 0
    visited = set([])
    current = start
    queue = []

    while True:
        dist = distances[current]
        nbs = neighbors(current,N,M)
        for nb in nbs:
            if nb in visited: continue
            (nb_i, nb_j) = nb
            if distances[nb] > dist + arr[nb_i, nb_j]:
                distances[nb] = dist + arr[nb_i, nb_j]
                bisect.insort(queue, (distances[nb],nb))
        visited.add(current)
        if current == end:
            break
        foundNewCurrent = False
        while not foundNewCurrent:
            d, current = queue.pop(0)
            if current not in visited and d <= distances[current]:
                foundNewCurrent = True

    print(distances[end])

if __name__ == '__main__':
    arr = process_input('input.txt')
    N = len(arr)
    M = len(arr[0])
    start = (0,0)
    end = (N-1, M-1)
    dijkstra(start, end, arr, N, M)

