def range_copy(start, end, step=1):
    while start != end:
        yield start
        start += step


# print(range(10))
x = range_copy(0, 10, 1)
for _ in range_copy(0, 10, 1):
    print(next(x))


def add_two(x):
    return x + 2


def map_copy(func, coll):
    for i in coll:
        yield func(i)


#
x = map_copy(add_two, [1, 2, 3, 4, 5])
for _ in range(5):
    print(next(x))


def enumerate_copy(coll):
    for i in range(len(coll)):
        yield (i, coll[i])


x = enumerate_copy([1, 2, 3, 4, 5, ])
for i in range(5):
    print(next(x))


def zip_copy(x, y):
    try:
        for i in range(len(x)):
            yield (x[i], y[i])
    except IndexError as e:
        pass


x = zip_copy('abcf', [1, 2, 3, 4])
for i in range(4):
    print(next(x))
