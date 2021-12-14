import numpy as np

def process_input(file_path):
    f = open(file_path)
    lines = f.readlines()
    f.close()

    n_pairs = len(lines[2:])

    pair_list = []
    generated_list = []
    pair_idx_map = {}

    char_list = []
    char_idx_map = {}
    char_idx = 0

    generated_pair_list = []
    for idx, line in enumerate(lines[2:]):
        pair, generated = [s.strip() for s in line.strip().split('->')]
        
        pair_tuple = (pair[0], pair[1])

        for c in pair_tuple:
            if c not in char_idx_map:
                char_list.append(c)
                char_idx_map[c] = char_idx
                char_idx += 1

        pair_idx_map[pair_tuple] = idx
        pair_list.append(pair_tuple)
        
        generated_pairs = [(pair_tuple[0], generated), (generated, pair_tuple[1])]
        generated_list.append(generated_pairs)

    update_pair_count_arr = np.zeros((n_pairs, n_pairs))
    for old_pair in pair_list:
        old_pair_idx = pair_idx_map[old_pair]
        for generated_pair in generated_list[old_pair_idx]:
            generated_pair_idx = pair_idx_map[generated_pair]
            update_pair_count_arr[generated_pair_idx][old_pair_idx] += 1

    template_string = lines[0].strip()
    pair_counts = np.zeros((n_pairs))
    for i in range(len(template_string) - 1):
        pair = (template_string[i], template_string[i+1])
        pair_idx = pair_idx_map[pair]
        pair_counts[pair_idx] += 1

    first_elem = template_string[0]
    last_elem = template_string[-1]

    return pair_counts, update_pair_count_arr, pair_list, pair_idx_map, char_list, char_idx_map, first_elem, last_elem

def pair_counts_to_char_counts(pair_counts, pair_list, char_idx_map, first_elem, last_elem):
    char_counts = np.zeros((len(char_idx_map)))
    for pair_idx, pair_count in enumerate(pair_counts):
        char_counts[char_idx_map[pair_list[pair_idx][0]]] += pair_count
        char_counts[char_idx_map[pair_list[pair_idx][1]]] += pair_count
    char_counts[char_idx_map[first_elem]] += 1
    char_counts[char_idx_map[last_elem]] += 1
    char_counts = char_counts / 2
    return char_counts

if __name__ == '__main__':
    pair_counts, update_pair_count_arr, pair_list, pair_idx_map, char_list, char_idx_map, first_elem, last_elem = process_input('input.txt')
    steps = 40
    pair_counts = np.linalg.matrix_power(update_pair_count_arr, steps) @ pair_counts
    char_counts = pair_counts_to_char_counts(pair_counts, pair_list, char_idx_map, first_elem, last_elem)
    print(np.max(char_counts) - np.min(char_counts))
