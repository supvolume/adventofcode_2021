txt = open("input_day07.txt", 'r').read()
txt_list = txt.split(",")
int_list = list(map(int, txt_list))

all_position = list(set(sorted(int_list)))
start_po = 0
shortest = 0
found = False
max_length = max(all_position)**2


# Part 1
def find_length(position, all_list):
    sum_length = 0
    for i in all_list:
        sum_length += abs(position - i)
    return sum_length
        
while found == False:
    sum_length = find_length(all_position[start_po], sorted(int_list))
    if sum_length < max_length:
        max_length = sum_length
        start_po += 1
    else:
        found = True
        print(max_length)


