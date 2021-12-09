def process_input(input_path):
    f = open(input_path)
    arr = []
    for line in f.readlines():
        row = []
        for char in line.strip():
            row.append(int(char))
        arr.append(row)
    f.close()
    N = len(arr)
    M = len(arr[0])
    return N, M, arr

def neighbors(i,j, N, M):
    nbs = []
    if i != N-1:
        nbs.append((i+1,j))
    if i != 0:
        nbs.append((i-1,j))
    if j != M-1:
        nbs.append((i,j+1))
    if j != 0:
        nbs.append((i,j-1))
    return nbs
 
basin_count = 0
basin_map = {}
basin_index = 0

def do_search(i,j,N,M,arr):
    global basin_index, basin_count, basin_map
    if(arr[i][j] == 9):
        basin_map[(i,j)] = -1
        return False
    if (i,j) in basin_map:
        return True
    basin_map[(i,j)] = basin_index
    basin_count += 1
    nbs = neighbors(i,j, N, M)
    for nb in nbs:
        do_search(nb[0], nb[1], N, M, arr)
    return True

if __name__ == '__main__':
    N, M, depth_array = process_input('input.txt')
    first_largest = 0
    second_largest = 0
    third_largest = 0
    for i in range(N):
        for j in range(M):
            if (i,j) not in basin_map:
                if do_search(i,j, N, M, depth_array):
                    if basin_count > first_largest:
                        third_largest = second_largest
                        second_largest = first_largest
                        first_largest = basin_count
                    elif basin_count > second_largest:
                        third_largest = second_largest
                        second_largest = basin_count
                    elif basin_count > third_largest:
                        third_largest = basin_count
                    basin_count = 0
                    basin_index += 1

    print(first_largest * second_largest * third_largest)
