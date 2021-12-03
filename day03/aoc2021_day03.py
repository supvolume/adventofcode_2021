txt = open("input_day03.txt", 'r').read()
txt_list = txt.split("\n")

# Part 1
def dominate_bit(bit_list):
    # Sum each column
    col_n = len(bit_list[0])
    sum_bit = [0]*col_n
    for row in bit_list:
        for col in range(col_n):
            sum_bit[col] += int(row[col])

    # Find the most common bit
    gamma = ""
    epsilon = ""
    for i in sum_bit:
        if i >= len(bit_list)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon

gamma, epsilon = dominate_bit(txt_list)
print("part 1 ans: ", int(gamma, 2) * int(epsilon, 2))


# Part 2
oxygen = txt_list.copy()
co2 = txt_list.copy()
temp_o2 = []
temp_co2 = []
for i in range(len(txt_list[0])):
    more_bit, _ = dominate_bit(oxygen)
    _, less_bit = dominate_bit(co2)
    
    if len(oxygen) > 1:
        for bit in oxygen:
            if bit[i] == more_bit[i]:
                temp_o2.append(bit)
        oxygen = temp_o2
        temp_o2 = []
            
    if len(co2) > 1:
        for bit in co2:
            if bit[i] == less_bit[i]:
                temp_co2.append(bit)
            
        co2 = temp_co2
        temp_co2 = []
        
print("part 2 ans: ", int(oxygen[0], 2) * int(co2[0], 2))
