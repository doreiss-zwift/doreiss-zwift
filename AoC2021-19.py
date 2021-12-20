from collections import deque
import numpy as np

def D(a, b): return sum(abs(aa-bb) for aa, bb in zip(a, b))

def correspond(s1, s2):
    matching_beacons = [(r1, r2) for r1 in s1 for r2 in s2
               if len(set([D(r1, r) for r in s1]) & set([D(r2, r) for r in s2])) >= 12]

    if len(matching_beacons) == 0:
        return False, (0,0,0)

    x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    rotations = [np.eye(3), x, y, x@x, x@y, y@x, y@y, x@x@x,
                 x@x@y, x@y@x, x@y@y, y@x@x, y@y@x, y@y@y,
                 x@x@x@y,x@x@y@x, x@x@y@y, x@y@x@x, x@y@y@y,
                 y@x@x@x, y@y@y@x, x@x@x@y@x, x@y@x@x@x, x@y@y@y@x]
    
    scanner_rotation = np.eye(3)
    for rotation in rotations:
        if len(set([tuple(r1 - (r2 @ rotation)) for r1, r2 in matching_beacons])) == 1:
            scanner_rotation = rotation
            break

    scanner_position = matching_beacons[0][0] - matching_beacons[0][1] @ scanner_rotation

    return True, scanner_position

def process_input(path):
    f = open(path)
    lines = [line.strip() for line in f.readlines()]
    f.close()

    scanner_vecs = []
    idx = -1
    for line in lines:
        if line == '':
            continue
        if line[0:3] == '---':
            idx += 1
            scanner_vecs.append([])
        else:
            scanner_vecs[idx].append(np.array([int(s) for s in line.split(',')]))
    return scanner_vecs

if __name__ == '__main__':
    scanner_vecs = process_input('input.txt')

    found_scanners = [scanner_vecs[0]]
    scanners_to_search = deque(scanner_vecs[1:])
    found_scanner_positions = [(0, 0, 0)]

    while len(scanners_to_search):
        scanner = scanners_to_search.popleft()
        found = False
        for found_scanner in found_scanners:
            found, found_scanner_position = correspond(found_scanner, scanner)
            if found:
                found_scanner_positions.append(found_scanner_position)
                found_scanners.append(scanner)
                break
        if not found:
            scanners_to_search.append(scanner)

    print(max(D(s1, s2)
      for s1 in found_scanner_positions for s2 in found_scanner_positions))
