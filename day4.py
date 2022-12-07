def part1(input_file):
    overlap_count = 0
    with open(input_file) as f:
        assignments = f.readlines()
    for pair in assignments:
        pair_array = list()
        pair = pair.replace("\n", "")
        pair_assignments = pair.split(',')
        for assignment in pair_assignments:
            assignment_start_stop = assignment.split('-')
            assignment_start_stop[0] = int(assignment_start_stop[0])
            assignment_start_stop[1] = int(assignment_start_stop[1])
            pair_array.append(assignment_start_stop)
        if (pair_array[0][0] <= pair_array[1][0] and pair_array[0][1] >= pair_array[1][1]) or (pair_array[0][0] >= pair_array[1][0] and pair_array[0][1] <= pair_array[1][1]):
            overlap_count = overlap_count + 1
    return overlap_count

def part2(input_file):
    overlap_count = 0
    with open(input_file) as f:
        assignments = f.readlines()
    for pair in assignments:
        pair_array = list()
        pair = pair.replace("\n", "")
        pair_assignments = pair.split(',')
        for assignment in pair_assignments:
            assignment_start_stop = assignment.split('-')
            assignment_start_stop[0] = int(assignment_start_stop[0])
            assignment_start_stop[1] = int(assignment_start_stop[1])
            pair_array.append(assignment_start_stop)
        if (pair_array[0][0] >= pair_array[1][0] and pair_array[0][0] <= pair_array[1][1]) \
                or (pair_array[0][1] >= pair_array[1][0] and pair_array[0][1] <= pair_array[1][1]) \
                or (pair_array[1][0] >= pair_array[0][0] and pair_array[1][0] <= pair_array[0][1]) \
                or (pair_array[1][1] >= pair_array[0][0] and pair_array[1][1] <= pair_array[0][1]):
            overlap_count = overlap_count + 1
    return overlap_count