N = 5

winners = [set([0, 1, 2, 3, 4]),    set([5, 6, 7, 8, 9]),    set([10, 11, 12, 13, 14]), set([15, 16, 17, 18, 19]), set([20, 21, 22, 23, 24]),
		   set([0, 5, 10, 15, 20]), set([1, 6, 11, 16, 21]), set([2, 7, 12, 17, 22]),   set([3, 8, 13, 18, 23]),   set([4, 9, 14, 19, 24])]

f = open("input.txt")
lines = f.readlines()
row = 0
num_boards = 0

bingo_boards_as_maps = [] 
bingo_board_map = {}

for line_idx, line in enumerate(lines):
	if line_idx == 0:
		bingo_nums = np.array([int(s) for s in line.strip().split(',')], dtype=int)
	else:
		if row == 0:
			row += 1
		else:
			bingo_row = [int(s) for s in line.rstrip().split()]
			for idx, elem in enumerate(bingo_row):
				bingo_board_map[elem] = (row - 1) * N + idx
			row += 1
			if row == (N + 1):
				row = 0
				bingo_boards_as_maps.append(bingo_board_map)
				num_boards += 1
				bingo_board_map = {}
f.close()

def part1():
	called_position_per_board = [set() for i in range(len(bingo_boards_as_maps))]
	for num in bingo_nums:
		for board_idx, bingo_board in enumerate(bingo_boards_as_maps):
			if num in bingo_board:
				called_position_per_board[board_idx].add(bingo_board[num])
				for winner in winners:
					if winner.intersection(called_position_per_board[board_idx]) == winner:
						numbers = list(bingo_board.keys())
						positions = list(bingo_board.values())
						s = 0
						for idx, pos in enumerate(positions):
							if pos not in called_position_per_board[board_idx]: 
								s += numbers[idx]
						return s * num

def part2():
	eliminated_boards = set()
	eliminated_board_scores = {}
	last_eliminated = 0
	called_position_per_board = [set() for i in range(len(bingo_boards_as_maps))]
	for num in bingo_nums:
		for board_idx, bingo_board in enumerate(bingo_boards_as_maps):
			if board_idx not in eliminated_boards:
				if num in bingo_board:
					called_position_per_board[board_idx].add(bingo_board[num])
					for winner in winners:
						if winner.intersection(called_position_per_board[board_idx]) == winner:
							numbers = list(bingo_board.keys())
							positions = list(bingo_board.values())
							s = 0
							for idx, pos in enumerate(positions):
								if pos not in called_position_per_board[board_idx]: 
									s += numbers[idx]
							eliminated_board_scores[board_idx] = s * num
							eliminated_boards.add(board_idx)
							last_eliminated = board_idx
	return eliminated_board_scores[last_eliminated]


print("Part1:", part1())
print("Part2:", part2())
