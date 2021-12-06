txt = open("input_day06.txt", 'r').read()
txt_list = txt.split(",")
timer_list = list(map(int, txt_list))


final_day = 256 # Change to 80 for part 1 solution

# Fish amount of the current week
# Each index represent the number of the day
# The number in each index is the number of the fish that will create
# new fish on that day
week = [0,0,0,0,0,0,0]
# The amount of new fish that born and not ready to give birth in last week
# Have to combine with "week" amount when reach it's day
wait = [0,0,0,0,0,0,0]
# The amount of new fish that born and not ready to give birth in last week
# (which need to wait 2 more day than old fish)
wait_next = [0,0,0,0,0,0,0]

for i in timer_list:
    week[i] += 1


for day in range(final_day):
    week[day%7] += wait[day%7]
    wait[day%7] = wait_next[day%7]
    wait_next[(day+2)%7] = week[(day)%7]
    wait_next[day%7] = 0
    

print(sum(week+wait+wait_next))

