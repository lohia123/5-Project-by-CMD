list1 = [78, 12, 53, 58, 47, 99, 14, 26, 23, 31, 41, 79]

even = tuple(filter((lambda x: x % 2 == 0), list1))

print(even)