def process_input(file_path):
    f = open(file_path)
    lines = f.readlines()
    f.close()

    edges = {}
    for line in lines: 
        vertex1, vertex2 = line.strip().split('-')
        if vertex1 not in edges:
            edges[vertex1] = set([vertex2])
        else:
            edges[vertex1].add(vertex2)
        if vertex2 not in edges:
            edges[vertex2] = set([vertex1])
        else:
            edges[vertex2].add(vertex1)

    return edges

def count_paths(start, end, already_visited, has_visited_twice, edges):
    if start == end:
        return 1, [[end]]

    undo1 = False
    undo2 = False
    if start.islower():
        if start in already_visited:
            has_visited_twice = True
            undo2 = True
        else:
            already_visited.add(start)
            undo1 = True

    path_counter = 0
    paths = []
    for v in edges[start]:
        if ((v not in already_visited) or (not has_visited_twice)) and v != 'start':
            sub_counter, sub_paths = count_paths(v, end, already_visited, has_visited_twice, edges)
            path_counter += sub_counter
            paths += sub_paths
    for i in range(len(paths)):
        paths[i].append(start)

    if undo1:
        already_visited.remove(start)
    if undo2:
        has_visited_twice = False

    return path_counter, paths

if __name__ == '__main__':
    edges = process_input('input.txt')
    already_visited = set([])
    has_visited_twice = False
    path_counter, paths = count_paths('start', 'end', already_visited, has_visited_twice, edges)
    print(path_counter)
