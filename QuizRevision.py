walk_circle = 0
for walk_circle in range (1,10):
    print (walk_circle)
    if walk_circle==5:
        continue
print("walking complete")
print(walk_circle)


my_list = ['abc', 123, True, [0,1,2], 'fff', -1, -500]

print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[:5:2])
print('abd' in my_list)
print(my_list[0])


fruits = ["Apple", "Banana", "Carrot"]

for fruit in fruits:
    print(fruit)


list1 = [[1, 2], [3, 4]]

list2 = list1.copy()

list2[0][0] = 99
print(list1)
print(list2)

import copy
list3 = [[1, 2], [3, 4]]

list4 = copy.deepcopy(list3)
list4[0][0] = 99
print(list1)
print(list2)