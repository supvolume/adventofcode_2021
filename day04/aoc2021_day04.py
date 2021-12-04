import copy

txt = open("input_day04.txt", 'r').read()
txt_list = txt.split("\n\n")

# Part 1
draw_number = txt_list[0].split(",")
bingos = []
for i in txt_list[1:]:
    each_bing = []
    for j in i.split("\n"):
        row = []
        for k in j.split(" "):
            if k != "":
                row.append(k)
        each_bing.append(row)        
    bingos.append(each_bing)
bingos2 = copy.deepcopy(bingos)  # for part 2

# Find a row or col that has bingo
def check_bingo(bingo, row, col):
    check_row = 0
    check_col = 0
    for i in range(5):
        if "c" in bingo[row][i]:
            check_row += 1
        if "c" in bingo[i][col]:
            check_col += 1
            
    if check_row == 5 or check_col == 5:
        return True

# match the number on the card and the draw card, then mark "c"        
def check_draw(bingo, draw_n):
    for row in range(5):
        for col in range(5):
            if bingo[row][col] == draw_n:
                bingo[row][col] += "c"
                if check_bingo(bingo, row, col) == True:
                    return True

# Check until find bingo card                    
def play_bingo(draw_number, bingos):      
    for n in draw_number:
        for i in bingos:
            if check_draw(i, n) == True:
                return n, i

n, win_bingo = play_bingo(draw_number, bingos)

not_call = 0
for i in win_bingo:
    for j in i:
        if "c" not in j:
            not_call += int(j)

print("Part 1 ans: ", int(n)*not_call)



# Part 2
# Check all of the cards until all the cards win
def last_win(draw_number, bingos):
    win_bin = []
    win_num = ""
    for n in draw_number:
        for i in bingos:
            if (check_draw(i, n) == True) and (i not in win_bin):
                win_bin.append(i)
                win_num = n
            if len(win_bin) == len(bingos):
                return win_num, win_bin[-1]


n, win_bingo = last_win(draw_number, bingos2)

not_call = 0
for i in win_bingo:
    for j in i:
        if "c" not in j:
            not_call += int(j)

print("Part 2 ans: ", int(n)*not_call)
