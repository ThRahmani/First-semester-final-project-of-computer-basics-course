import math


class LCG:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def generate_random(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state / float(self.m)


def generate_decimal_random_from_a_to_b(a: float, b: float):
    seed_value = abs(hash(str(a + b)))
    lcg_generator = LCG(seed=seed_value)
    return lcg_generator.generate_random() * (b - a) + a


def generate_random_from_a_to_b(a: float, b: float):
    seed_value = abs(hash(str(a + b)))
    lcg_generator = LCG(seed=seed_value)
    if a <= int(lcg_generator.generate_random() * (b - a) + a) <= b:
        return int(lcg_generator.generate_random() * (b - a) + a)


def normal_distribution(x):
    power = (-0.5)*(x**2)
    y = (math.e**power)/(math.sqrt(2*math.pi))
    return y


def generate_normal_random(n: int):
    normal_random_values = []
    for i in range(1, n+1):
        seed_value = abs(hash(str(i)))
        lcg_generator = LCG(seed=seed_value)
        normal_random_values.append(normal_distribution(lcg_generator.generate_random()))

    m = sum(normal_random_values)/n
    s = 0

    for num in normal_random_values:
        s = s + math.sqrt(((num-m)**2)/n)

    return {
        'Values': normal_random_values,
        'Mean': m,
        'Standard deviation': s
        }
