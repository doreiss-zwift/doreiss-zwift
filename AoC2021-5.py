from collections import defaultdict

drawnPtCounts = defaultdict(lambda: 0)

def IsSecondOccurance(pt):
    drawnPtCounts[pt] += 1
    if drawnPtCounts[pt] == 2:
       return True
    return False

f = open("input.txt")
lines = f.readlines()
pts = []
for line in lines:
    x1, y1, x2, y2 = [int(s) for s in line.strip().replace('->',',').split(',')]
    if x1 == x2:
        smallY, bigY = (y1, y2) if y1 < y2 else (y2, y1)
        for y in range(smallY, bigY+1):
            pts.append((x1, y))
    elif y1 == y2:
        smallX, bigX = (x1, x2) if x1 < x2 else (x2, x1)
        for x in range(smallX, bigX+1):
            pts.append((x, y1))
    else:
        firstX, firstY, secondX, secondY = (x1, y1, x2, y2) if x1 < x2 else (x2, y2, x1, y1)
        dY = 1 if firstY < secondY else -1
        for i in range(secondX - firstX + 1):
            pts.append((firstX + i, firstY + dY * i))
f.close()

totalDoubles = 0
for pt in pts:
    if IsSecondOccurance(pt):
        totalDoubles += 1
print(totalDoubles)
