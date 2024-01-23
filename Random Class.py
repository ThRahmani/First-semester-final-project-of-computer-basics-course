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
