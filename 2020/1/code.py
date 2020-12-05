# Advent of code Year 2020 Day 1 solution
# Author = ?
# Date = December 2020

import functools

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [int(line.strip()) for line in input_file.readlines()]

def part1(nums):
    witnessed = set()
    
    for num in nums:
        target = 2020 - num
        if target in witnessed:
            return (num, target)
        else:
            witnessed.add(num)
    return None

def part2(nums):
    # Store map of 2020 - n => [n]
    witnessed_nums = set()

    # map of 2020 - (n1 + n2) => [n1, n2]
    double_sums = {}

    for num in nums:
        target = 2020 - num
        if target in double_sums:
            return double_sums[target] + [num]
        else:
            for prev in witnessed_nums:
                partial_sum = prev + num
                double_sums[partial_sum] = [prev, num]
            witnessed_nums.add(num)
    return None

def main():
    part1_answer = functools.reduce(lambda x, y: x*y, part1(input))
    print(f'Part 1: {part1_answer}')

    part2_answer = functools.reduce(lambda x, y: x*y, part2(input))
    print(f'Part 2: {part2_answer}')

main()
