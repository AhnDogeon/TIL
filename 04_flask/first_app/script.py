import random

def pick_lotto():
    numbers = random.sample(range(1,46), 6) 
    return numbers

print(pick_lotto())