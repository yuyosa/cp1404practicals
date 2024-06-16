import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    num_picks = int(input("How many quick picks? "))

    for i in range(num_picks):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2d}" for num in pick))

def generate_quick_pick():
    pick = set()
    while len(pick) < NUMBERS_PER_PICK:
        pick.add(random.randint(MIN_NUMBER, MAX_NUMBER))
    return sorted(pick)

main()