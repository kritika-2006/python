# Normal tarika:
squares = []
for x in range(1, 11):
    squares.append(x**2)

# List Comprehension (Smart tarika):
squares_smart = [x**2 for x in range(1, 11)]

print(squares_smart)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]