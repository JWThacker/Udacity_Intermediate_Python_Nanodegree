import random
import functools

def genrange(n):
    i = 0
    while True:
        if i >= n:
            break
        yield i
        i += 1


def generate_tribonacci():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a , b, c = b, c, a + b + c

def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a , b = b, a + b

def random_list(size, start = 0, stop = 10):
    return list(random.randrange(start, stop) for _ in range(size))

def create_profile(given_name, *surnames, **details):
    name = given_name
    for surname in surnames:
        name += " " + surname
    print(name)
    for key, value in details.items():
        print(key, value, sep = ": ")

def upper(stringValue):
    return stringValue.upper()

def reverse(stringValue):
    return stringValue[::-1]

def generate_cases():
    size = 0
    while True:
        yield random_list(size)
        size += 1

def test_function(*args, **kwargs):
    return (args, kwargs)

def memoize(function):
    function._cache = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in function._cache:
           function._cache[key] = function(*args, **kwargs)
        return function._caches[key]
    return wrapper

if __name__ == '__main__':
    # Practice with positional (required) and keyword (optional) arguments.
    print("Just a given name (a required argument).")
    create_profile("Sam")
    print("===========================")
    print("(required) given_name, (optional/positional) surnames, (optional keyword arguments) details.")
    create_profile("Martin", "Luther", "King", "Jr.", born = 1929, died = 1968)
    create_profile("Sebastian", "Thrun", cofounded = "Udacity", experience = "Stanford Professor")

    # map and lambda functions
    stringList = ["apple", "orange", "pear"]
    a = map(len, stringList)
    b = map(upper, stringList)
    c = map(reverse, stringList)
    d = map(lambda x: x[:2], stringList)
    print(list(a))
    print(list(b))
    print(list(c))
    print(list(d))

    # filter and lambda functions
    e = filter(lambda x: x % 3 == 0, range(100))
    f = filter(lambda x: x % 5 == 0, range(100))
    g = filter(lambda x: x % 15 == 0, range(100))
    h = filter(lambda x: x % 3 != 0 and x % 5 != 0, range(100))
    print(list(e))
    print(list(f))
    print(list(g))
    print(list(h))

    # Practice with the generate_cases() generator
    for case in generate_cases():
        if len(case) > 10:
            break
        print(case)

print(test_function(7, 8, z =2))

g = generate_fibonacci()
g3 = generate_tribonacci()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print('\n')
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))

gen_range = genrange(10)
print('\n')
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
print(next(gen_range))
