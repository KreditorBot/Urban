my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
c = int(0)
while c <= len(my_list):
    if my_list[c] >= 0 and my_list[c] != 0:
        print(my_list[c])
        c = c + 1
    elif my_list[c] == 0:
        c = c + 1
        continue
    else:
        break
