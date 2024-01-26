from numpy import random
import math


def random_integer_number_from_a_to_b(a, b):
    return random.randint(a, b)


def random_number_from_a_to_b(a, b):
    return random.random()*(b-a) + a


def normal_distribution(x):
    power = (-0.5)*(x**2)
    y = (math.e**power)/(math.sqrt(2*math.pi))
    return y


def generate_normal_random(n: int):
    normal_random_values = []
    for i in range(1, n+1):
        normal_random_values.append(normal_distribution(random.random()))

    m = sum(normal_random_values)/n
    s = 0

    for num in normal_random_values:
        s = s + math.sqrt(((num-m)**2)/n)

    return [
        ('Values:', normal_random_values),
        ('Mean:', m),
        ('Standard deviation:', s)
        ]
