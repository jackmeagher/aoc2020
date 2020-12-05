# Advent of code Year 2020 Day 2 solution
# Author = ?
# Date = December 2020

import re

parser = re.compile('^(\d+)-(\d+)\s*([a-z]):\s*(\w*)$')

def parse(line):
    match = parser.match(line.strip())
    return [int(match[1]), int(match[2]), match[3], match[4]]

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [parse(line) for line in input_file.readlines()]

#TEST_CASES = [
#    "1-3 a: abcde",
#    "1-3 b: cdefg",
#    "2-9 c: ccccccccc"
#]

#input = [parse(line) for line in TEST_CASES]

def part1(parsed_lines):
    valid = 0

    for parsed_line in parsed_lines:
        lower_bound, upper_bound, target_char, password = parsed_line

        target_char_count = 0
        for char in password:
            if char == target_char:
                target_char_count += 1

        if lower_bound <= target_char_count <= upper_bound:
            valid += 1

    return valid

def part2(parsed_lines):
    valid = 0

    for parsed_line in parsed_lines:
        first_pos, second_pos, target_char, password = parsed_line

        num_matching = 0

        first_present = password[first_pos - 1] == target_char
        second_present = password[second_pos - 1] == target_char

        if first_present != second_present:
            valid += 1

        #if first_pos == second_pos and first_present:
            #valid += 1

    return valid

def main():
    part1_answer = part1(input)
    print(f'Part 1: {part1_answer}')

    part2_answer = part2(input)
    print(f'Part 2: {part2_answer}')

main()
