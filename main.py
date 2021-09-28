maze = open("maze.txt", encoding="UTF-8").read().split('\n')

for i in range(len(maze)):
    if "@" in maze[i]:
        start_pos = sx, sy = (maze[i].index('@'), i)


def get_symbol(pos: tuple) -> str:
    return maze[pos[1]][pos[0]]


def can_go_in(pos: tuple) -> bool:
    return get_symbol(pos) != '#'


def is_final(pos: tuple) -> bool:
    return get_symbol(pos) == '$'


def find_paths(x, y, path):
    pos = (x, y)
    if not can_go_in(pos) or pos in path:
        return []

    if is_final(pos):
        return [path]

    path += [(pos)]

    return find_paths(x - 1, y, path) + \
           find_paths(x + 1, y, path) + \
           find_paths(x, y - 1, path) + \
           find_paths(x, y + 1, path)


print(find_paths(sx, sy, []), sep='\n')
