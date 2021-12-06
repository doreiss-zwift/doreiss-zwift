from collections import defaultdict

fish_map = defaultdict(lambda: 0)

f = open("input.txt")
init_fish_array = [int(s) for s in f.readlines()[0].split(',')]
f.close()

min_fish_value = 999
for fish in init_fish_array:
    fish_map[fish] += 1
    if fish < min_fish_value:
        min_fish_value = fish

elapsed_days = 0
total_days = 256
result = len(init_fish_array)
while True:
    tmp = defaultdict(lambda: 0)
    new_min_fish_value = 999
    elapsed_days += (min_fish_value + 1)
    if(elapsed_days > total_days):
        print(result)
        break
    for key in fish_map :
        if key == min_fish_value :
            tmp[8] += fish_map[min_fish_value]
            tmp[6] += fish_map[min_fish_value]
            result += fish_map[min_fish_value]
            if 6 < new_min_fish_value :
                new_min_fish_value = 6
        else:
            tmp[key - min_fish_value - 1] += fish_map[key]
            if key - min_fish_value - 1 < new_min_fish_value :
                new_min_fish_value = key - min_fish_value - 1
    fish_map = tmp
    min_fish_value = new_min_fish_value
