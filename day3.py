def get_priority(item):
    if ord(item) >= 96:
        priority = ord(item) - 96
    else:
        priority = ord(item) - 64 + 26
    return priority

def part1(input_file):
    sum_priority = 0
    with open(input_file) as f:
        rucksacks = f.readlines()
    for rucksack in rucksacks:
        print(rucksack)
        print(len(rucksack))
        rucksack = rucksack.replace("\n", "")
        compartment1 = rucksack[0:int(len(rucksack)/2)]
        compartment2 = rucksack[int(len(rucksack)/2):len(rucksack)]
        for item1 in compartment1:
            for item2 in compartment2:
                if item1 == item2:
                    duplicate = item1
        sum_priority = sum_priority + get_priority(duplicate)
    return sum_priority

def part2(input_file):
    sum_priority = 0
    with open(input_file) as f:
        rucksacks = f.readlines()
    group_count = int(len(rucksacks) / 3)
    group = 0
    while group < group_count:
        group_rucksacks = list()
        group_rucksacks.append(rucksacks[group * 3].replace("\n", ""))
        group_rucksacks.append(rucksacks[group * 3 + 1].replace("\n", ""))
        group_rucksacks.append(rucksacks[group * 3 + 2].replace("\n", ""))
        for item1 in group_rucksacks[0]:
            for item2 in group_rucksacks[1]:
                if item1 == item2:
                    for item3 in group_rucksacks[2]:
                        if item1 == item3:
                            duplicate = item1
        sum_priority = sum_priority + get_priority(duplicate)
        group = group + 1
    return sum_priority