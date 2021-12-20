import numpy as np

def process_input(path):
    f = open(path)
    lines = [line.strip() for line in f.readlines()]
    f.close()

    N = 512
    image_enhancement = {}
    for i in range(N):
        image_enhancement[i] = 0 if lines[0][i] == '.' else 1

    image = []
    for line in lines[2:]:
        row = []
        for c in line:
            if c == '.':
                row.append(0)
            else:
                row.append(1)
        image.append(row)
    image = np.array(image, dtype=int)
    rows, cols = np.shape(image)

    return image_enhancement, image, rows, cols

def neighbors(i,j):
    return [(i+1,j+1), (i+1,j), (i+1,j-1), (i,j+1), (i,j), (i,j-1), (i-1,j+1), (i-1,j), (i-1,j-1)]

def compute_lookup(i, j, image):
    nbs = neighbors(i,j)
    lookup = 0
    power = 1
    for nb in nbs:
        lookup += power * image[nb[0],nb[1]]
        power *= 2
    return lookup

def enhance_image(image, image_enhancement, fill_val):
    enhanced_image = np.full(np.shape(image), fill_val, dtype=int)
    rows, cols = np.shape(enhanced_image)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            lookup = compute_lookup(i,j, image)
            enhanced_image[i,j] = image_enhancement[lookup]
    return enhanced_image

if __name__ == '__main__':
    image_enhancement, image, rows, cols = process_input('input.txt')


    STEPS = 50
    fill_val = 0
    for step in range(STEPS):
        new_rows = rows + 4
        new_cols = cols + 4
        new_image = np.full((new_rows, new_cols), fill_val, dtype=int)
        new_image[2:-2, 2:-2] = image
        fill_val = image_enhancement[0 if fill_val == 0 else 511]
        new_image = enhance_image(new_image, image_enhancement, fill_val)
        
        image = new_image
        rows = new_rows
        cols = new_cols
        print(step, "...")

    print(np.sum(image))
