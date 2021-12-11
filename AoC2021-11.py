def neighbors(i,j, N, M):
    nbs = []
    for (di,dj) in [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        (newI, newJ) = (i + di, j + dj)
        if newI < N and newI >= 0 and newJ < M and newJ >= 0:
            nbs.append((newI, newJ))
    return nbs

def do_increment(arr,N,M):
    flash_set = set()
    for i in range(N):
        for j in range(M):
            arr[i][j] += 1
            if arr[i][j] > 9:
                flash_set.add((i,j))

    return arr, flash_set

def do_flashing(arr, flash_set, has_flashed, flash_counter, N, M):
    new_flash_set = set()
    for elem in flash_set:
        if elem not in has_flashed:
            has_flashed.add(elem)
            flash_counter += 1
            for nb in neighbors(elem[0],elem[1], N, M):
                arr[nb[0]][nb[1]] += 1
                if arr[nb[0]][nb[1]] > 9:
                    if nb not in flash_set and nb not in has_flashed:
                        new_flash_set.add(nb)
    return arr, new_flash_set, has_flashed, flash_counter
    

def do_resetting(arr,N,M):
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 9:
                arr[i][j] = 0
    return arr

def process_input(file_path):
    f = open(file_path)
    lines = f.readlines()
    light_arr = []
    for line in lines: 
        row = []
        for c in line.strip():
            row.append(int(c))
        light_arr.append(row)
    f.close()
    return len(light_arr), len(light_arr[0]), light_arr

if __name__ == '__main__':
    N, M, light_arr = process_input('input.txt')
    turn = 0
    flash_counter = 0
    while(True):
        turn += 1
        light_arr, flash_set = do_increment(light_arr, N, M)
        has_flashed = set()
        while len(flash_set) != 0:
           light_arr, flash_set, has_flashed, flash_counter = do_flashing(light_arr, flash_set, has_flashed, flash_counter, N, M)
        light_arr = do_resetting(light_arr, N, M)
        if(len(has_flashed) == N * M):
            print(turn)
            break
