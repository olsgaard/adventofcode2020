from math import prod

open_square = '.'
tree = '#'

biome_map = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split('\n')


def count_trees(biome_map, slope_x = 3, slope_y = 1):
	xs = len(biome_map[0])
	x = 0

	n_trees = 0

	for line in biome_map[slope_y::slope_y]:
		x += slope_x
		n_trees += line[x%xs] == tree

	return n_trees

assert count_trees(biome_map) == 7, f"n_trees {n_trees}"

assert count_trees(biome_map, slope_x = 1) == 2
assert count_trees(biome_map, slope_x = 5) == 3
assert count_trees(biome_map, slope_x = 7) == 4
assert count_trees(biome_map, slope_x = 1, slope_y = 2) == 2

with open("input_day3.txt") as f:
	biome_map = [l.strip() for l in f.readlines()]

print(count_trees(biome_map))

print(prod([
	count_trees(biome_map, slope_x = 1, slope_y = 1),
	count_trees(biome_map, slope_x = 3, slope_y = 1),
	count_trees(biome_map, slope_x = 5, slope_y = 1),
	count_trees(biome_map, slope_x = 7, slope_y = 1),
	count_trees(biome_map, slope_x = 1, slope_y = 2),
	])
)
