with open('day1_input.txt') as f:
    lines = f.readlines()

elves = list()
elves.append(0)
elf = 0
for line in lines:
    line = line.replace("\n", "")
    if len(line) == 0:
        elf = elf + 1
        elves.append(0)
    else:
        calorie = int(line)
        elves[elf] = elves[elf] + calorie

elves.sort(reverse=True)
most_calories=elves[0]
print(most_calories)

top_three=elves[0]+elves[1]+elves[2]
print(top_three)
