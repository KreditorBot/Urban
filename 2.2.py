first = input()
second = input()
third = input()
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    first != second or first != third or second != third
    print(0)
