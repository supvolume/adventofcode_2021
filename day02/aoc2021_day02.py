txt = open("input_day02.txt", 'r').read()
txt_list = txt.split("\n")

# Part 1 answer
horizontal = 0
vertical = 0
for i in txt_list:
    if i[:-1] == "forward ":
        horizontal += int(i[-1])
    elif i[:-1] == "down ":
        vertical += int(i[-1])
    elif i[:-1] == "up ":
        vertical -= int(i[-1])
print("part 1 ans: ", horizontal * vertical)


# Part 2 answer
aim = 0
horizontal = 0
depth = 0
for i in txt_list:
    if i[:-1] == "forward ":
        horizontal += int(i[-1])
        depth += int(i[-1])*aim
    elif i[:-1] == "down ":
        aim += int(i[-1])
    elif i[:-1] == "up ":
        aim -= int(i[-1])
print("part 2 ans: ", horizontal*depth)
