txt = open("input_day05.txt", 'r').read()
txt_list = txt.split("\n")

# Part 1
# Clean and find max num
max_num = 0
lines = []
for i in txt_list:
    vents = []
    for j in i.split(" -> "):
        int_vent = []
        for k in j.split(","):
            int_vent.append(int(k))
            if int(k) > max_num:
                max_num = int(k)
        vents.append(int_vent)
    lines.append(vents)

# Create diagram
coor = [[0]*(max_num+1) for x in range(max_num+1)]

# Find vents
for line in lines:
    if line[0][0] == line[1][0]:
        position = sorted([line[0][1], line[1][1]])
        for i in range(position[0], position[1]+1):
            coor[i][line[0][0]] += 1
    elif line[0][1] == line[1][1]:
        position = sorted([line[0][0], line[1][0]])
        for i in range(position[0], position[1]+1):
            coor[line[0][1]][i] += 1

flat = [i for sub in coor for i in sub]

count = 0
for i in flat:
    if i >1:
        count+=1

print(count)

