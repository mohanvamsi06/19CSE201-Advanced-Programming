new_list = [56, 57, 58]

print(new_list)
new_list.append(59)
print(new_list)
new_list.append(60)
print(new_list)
new_list.insert(0, 55)
print(new_list)

new_list.remove(55)
print(new_list)
new_list.pop(4)
print(new_list)
new_list.pop(3)
print(new_list)

new_list2 = list(new_list)
print(new_list)
print(new_list2)