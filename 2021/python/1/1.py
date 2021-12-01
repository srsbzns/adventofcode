from typing import Iterator


with open('input.txt', 'r') as f:
    input = f.read()

report = input.splitlines()

i = 1
depth_increase_counter = 0

while i < len(report):
    if int(report[i-1]) < int(report[i]):
        print(report[i], ' is bigger than ', report[i-1])
        depth_increase_counter += 1
    i += 1

print(depth_increase_counter)