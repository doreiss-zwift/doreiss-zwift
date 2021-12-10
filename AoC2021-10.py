openings = ['{', '[', '(', '<']
closings = {'{' : '}', '[' : ']', '(' : ')', '<' : '>'}
points = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

def process_input(file_path):
    f = open(file_path)
    lines = f.readlines()
    f.close()
    return lines

if __name__ == '__main__':
    subsystem_lines = process_input('input.txt')
    scores = []
    for subsystem_line in subsystem_lines:
        stack = []
        corrupted = False
        for idx, c in enumerate(subsystem_line.strip()):
            if not corrupted:
                processed = False
                for opening in openings:
                    if not processed and c == opening:
                        stack.append(closings[opening])
                        processed = True
                if not processed:
                    processed = True
                    must_close = stack.pop()
                    if c != must_close:
                        corrupted = True
                        processed = True
                        continue
                if idx == len(subsystem_line.strip()) - 1:
                    score = 0
                    while len(stack) != 0:
                        score *= 5
                        score += points[stack.pop()]
                    scores.append(score)

    print(sorted(scores)[len(scores)//2])
