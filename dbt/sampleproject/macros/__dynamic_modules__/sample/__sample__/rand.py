from random import random
from math import ceil
def _private_implementation_random(scale):
    return ceil(random() * scale)

def generate_random_int(scale):
    return _private_implementation_random(scale)