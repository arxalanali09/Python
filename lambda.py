numbers = [1, 2, 3, 4, 5]

square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))

print("Squared:", square)
print("Cubed:", cube)
