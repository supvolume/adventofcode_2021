txt = open("input_day01.txt", 'r').read()
txt_list = txt.split("\n")
int_list = list(map(int, txt_list))

# Part 1 answer
def find_increase(num_list):
    prv_num = num_list[0]
    count = 0
    for i in num_list[1:]:
        if prv_num < i:
            count += 1
        prv_num = i
    return count
print("part 1: ", find_increase(int_list))

# Part 2 answer
start_win = 0
window_list = []
while start_win+2 < len(int_list):
    window_list.append(int_list[start_win] \
                       + int_list[start_win+1] \
                       + int_list[start_win+2])
    start_win += 1


print("part 2: ", find_increase(window_list))
