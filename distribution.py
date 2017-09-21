import math
import random


def spherical_sampler(size):
    sphere_distribution = [random.random() for i in range(size)]
    squared_rooted = math.sqrt(sum(i ** 2 for i in sphere_distribution))
    sphere = [i / squared_rooted for i in sphere_distribution]
    return sphere


def boolean_sampler(size):
    return [random.randint(0, 1) for i in range(size)]


ALLOWED_DISTRIBUTIONS = {
    "bool": boolean_sampler,
    "sphere": spherical_sampler
}