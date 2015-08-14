my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3
yet_another_tuple = 1, 2, 3, 4, 5
print(yet_another_tuple.__class__)

try:
    my_tuple[1] = 3
except TypeError:
    print "cannot modify a tuple"


def sum_and_product(x, y):
    return (x + y),( x * y)

sp = sum_and_product(2, 3)
print(sp)
s, p = sum_and_product(5, 10)

x, y = 1, 2
x, y = y, x

