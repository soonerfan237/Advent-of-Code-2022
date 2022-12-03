def part1(input_file):
    #A for Rock, B for Paper, and C for Scissors
    #X for Rock, Y for Paper, and Z for Scissors
    with open(input_file) as f:
        lines = f.readlines()
    points = 0
    for line in lines:
        opponent_shape = line[0]
        my_shape = line[2]
        if my_shape == 'X':
            points = points + 1
            if opponent_shape == 'C':
                points = points + 6
            elif opponent_shape == 'A':
                points = points + 3
        elif my_shape == 'Y':
            points = points + 2
            if opponent_shape == 'A':
                points = points + 6
            elif opponent_shape == 'B':
                points = points + 3
        elif my_shape == 'Z':
            points = points + 3
            if opponent_shape == 'B':
                points = points + 6
            elif opponent_shape == 'C':
                points = points + 3
    return points

def part2(input_file):
    #A for Rock, B for Paper, and C for Scissors
    #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    with open(input_file) as f:
        lines = f.readlines()
    points = 0
    for line in lines:
        opponent_shape = line[0]
        result = line[2]
        if result == 'X':
            if opponent_shape == 'A':
                points = points + 3
            elif opponent_shape == 'B':
                points = points + 1
            elif opponent_shape == 'C':
                points = points + 2
        elif result == 'Y':
            points = points + 3
            if opponent_shape == 'A':
                points = points + 1
            elif opponent_shape == 'B':
                points = points + 2
            elif opponent_shape == 'C':
                points = points + 3
        elif result == 'Z':
            points = points + 6
            if opponent_shape == 'A':
                points = points + 2
            elif opponent_shape == 'B':
                points = points + 3
            elif opponent_shape == 'C':
                points = points + 1
    return points

print(part1('day2_input.txt'))
print(part2('day2_input.txt'))