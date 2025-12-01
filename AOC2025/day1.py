from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
infile_path = BASE_DIR/"inputs/day1.txt"

pointer = 50 # starts at position 50
zero_count = 0 # how many times zero appears


with open(infile_path, "r") as infile:
    for line in infile:
        direction = line.strip()[0] # first
        distance = int(line.strip()[1::]) # anything but first
        effective_distance = distance % 100 
        if direction == "L":
            pointer = (pointer - effective_distance) % 100
        else:
            pointer = (pointer + effective_distance) % 100
        if pointer == 0:
            zero_count += 1
    print(zero_count)
