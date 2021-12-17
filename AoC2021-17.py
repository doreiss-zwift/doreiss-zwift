def propagate(r, v, xmin, xmax, ymin, ymax):
    if r[0] > xmax or r[1] < ymin: return 0
    if r[0] >= xmin and r[1] <= ymax: return 1
    newR = (r[0] + v[0], r[1] + v[1])
    newV = (v[0] - (v[0] > 0), v[1] - 1)
    return propagate(newR, newV, xmin, xmax, ymin, ymax)

def process_input(file_path):
    f = open(file_path)
    (xmin, xmax, ymin, ymax) = [int(s) for s in f.readline().strip().split(" ")]
    f.close()
    return xmin, xmax, ymin, ymax

if __name__ == '__main__':
    x_min, x_max, y_min, y_max= process_input('input.txt')

    sum = 0
    for vx in range(1,x_max+1):
        for vy in range(y_min, -y_min):
           sum += propagate((0,0), (vx, vy), x_min, x_max, y_min, y_max)

    print(sum)
