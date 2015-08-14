from random import randrange
if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"


x = randrange(0,9)
parity = "even" if x % 2 == 0 else "odd"
print(parity)

x = 0
while x < 10:
    print(x, "is less than 10")
    x += 1

for x in range(10):
    print(x, "is less than 10")

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)


