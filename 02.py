import re
from collections import defaultdict

with open('./inp/02.txt') as f:
    games = f.read().split('\n')

_sum = 0
power_sum = 0
for game in games:

    # Grab gameID
    gameId, rest = re.match(r"Game (\d+): (.+)", game).groups()
    gameId = int(gameId)

    # get cases as list (e.g.: '3 blue, 4 red')
    cases = rest.split('; ')

    game_possible = True
    max_colors = defaultdict(lambda: 0) # Part B <===
    for case in cases:
        
        color_count = defaultdict(lambda: 0)
        colors = case.split(', ')

        for c in colors: # e.g.: 3 blue
            
            num, c_string = c.split(' '); num = int(num)
            color_count[c_string] = num
            max_colors[c_string] = max(num, max_colors[c_string])

        if color_count['red'] > 12 or color_count['green'] > 13 or color_count['blue'] > 14:
            game_possible = False
    
    if game_possible: _sum += gameId
    power_sum += max_colors['red'] * max_colors['blue'] * max_colors['green']

# Answer A
print(_sum)

# Answer B
print(power_sum)



    
