


#list = [3,22,4,32,44,45,32,2,3,66,74,2,3,1]
# version of insertion sorting I wrote, probably not optimized
# Current position not neccessary, for loops reset the value with each iteration
'''
for item in range(1,len(list)):
    current_position = item
    while list[current_position] < list[current_position-1] and current_position > 0:
        list[current_position],list[current_position-1] = list[current_position-1],list[current_position]
        current_position = current_position-1
    print(item)

print(list)
'''
list = [3,22,4,32,44,45,32,2,3,66,74,2,3,1]

for item in range(1,len(list)):
    while list[item] < list[item-1] and item > 0:
        list[item],list[item-1],item = list[item-1],list[item],item-1

    print(item)

print(list)