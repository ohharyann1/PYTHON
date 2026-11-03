t1 = (56, 67, 99, 87, 31, 32)

new_list = []

for i in t1:
    if i % 2 != 0:
        new_list.append(i ** 3)

print(new_list)