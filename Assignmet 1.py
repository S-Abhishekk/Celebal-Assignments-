n = 5

print("Lower Triangle")
i = 1
while i <= n:
    print("*" * i)
    i += 1

print()
print("Upper Triangle")
j = n
while j > 0:
    print("*" * j)
    j -= 1

print()
print("Pyramid")
row = 1
while row <= n:
    space = " " * (n - row)
    star = "*" * (2 * row - 1)
    print(space + star)
    row += 1
