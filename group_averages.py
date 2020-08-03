mark_list=[[52,26,49,76,19,47],[14,45,98,83,49,25],[25,48,25,82,49,45]]
average_list=[]

def averager(a_list):
    total = 0
    for mark in a_list:
        total+=mark
        average= total / len(a_list)
    return average

def get_max(a_list):
    max = 0
    for mark in average_list:
        if mark > max:
            max = mark
    return max

for group_list in mark_list:
    average_mark = averager(group_list)
    average_list.append(average_mark)



max_value = get_max(average_list)


print(max_value)

