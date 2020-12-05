# Advent of code Year 2020 Day 3 solution
# Author = ?
# Date = December 2020

import functools

def parse_line(line):
    def is_tree(char):
        return char == '#'

    return [is_tree(char) for char in line]

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    tree_map = [parse_line(line.strip()) for line in input_file.readlines()]

def trees_hit_for_slope(tree_map, rise, run):
    x, y = 0, 0
    trees_hit = 0

    height = len(tree_map)
    width = len(tree_map[0])

    while y < height:
        if tree_map[y][x % width]:
            trees_hit += 1

        x += run
        y += rise

    return trees_hit

def part1(tree_map):
    return trees_hit_for_slope(tree_map, 1, 3)

def part2(tree_map):
    slopes = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]

    trees_hit = [trees_hit_for_slope(tree_map, *slope) for slope in slopes]

    return functools.reduce(lambda x, y: x * y, trees_hit)

def main():
    part1_answer = part1(tree_map)
    print(f'Part 1: {part1_answer}')

    part2_answer = part2(tree_map)
    print(f'Part 2: {part2_answer}')

main()
