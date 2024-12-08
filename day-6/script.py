from enum import Enum

INPUT_PATH = "input"
BOARD = None

class Direction(Enum):
    RIGHT = 1,
    LEFT = 2,
    UP = 3,
    DOWN = 4

class Action(Enum):
    STUCK = 1,
    LEFT = 2

def first_part():
    action = None
    while action is not Action.LEFT:
        if action is Action.STUCK:
            turn_right()
        direction = find_guard_direction()
        match direction:
            case Direction.LEFT:
                action = move_left()
            case Direction.RIGHT:
                action = move_right()
            case Direction.UP:
                action = move_up()
            case Direction.DOWN:
                action = move_down()
    return calculate_moves()

def calculate_moves():
    move_count = 0
    for row in BOARD:
        move_count += row.count("@")
    return move_count + 1

def move_left():
    x, y = find_guard()
    move_x = x - 1
    move_y = y
    while 0 <= move_x < len(BOARD[0]) and 0 <= move_y < len(BOARD):
        if check_obstacle(move_x, move_y):
            return Action.STUCK
        else:
            prev_x = move_x + 1
            BOARD[move_y][prev_x] = "@"
            BOARD[move_y][move_x] = "<"
        move_x -= 1
    else:
        return Action.LEFT

def move_right():
    x, y = find_guard()
    move_x = x + 1
    move_y = y
    while 0 <= move_x < len(BOARD[0]) and 0 <= move_y < len(BOARD):
        if check_obstacle(move_x, move_y):
            return Action.STUCK
        else:
            prev_x = move_x - 1
            BOARD[move_y][prev_x] = "@"
            BOARD[move_y][move_x] = ">"
        move_x += 1
    else:
        return Action.LEFT

def move_up():
    x, y = find_guard()
    move_x = x
    move_y = y - 1
    while 0 <= move_x < len(BOARD[0]) and 0 <= move_y < len(BOARD):
        if check_obstacle(move_x, move_y):
            return Action.STUCK
        else:
            prev_y = move_y + 1
            BOARD[prev_y][move_x] = "@"
            BOARD[move_y][move_x] = "^"
        move_y -= 1
    else:
        return Action.LEFT

def move_down():
    x, y = find_guard()
    move_x = x
    move_y = y + 1
    while 0 <= move_x < len(BOARD[0]) and 0 <= move_y < len(BOARD):
        if check_obstacle(move_x, move_y):
            return Action.STUCK
        else:
            prev_y = move_y - 1
            BOARD[prev_y][move_x] = "@"
            BOARD[move_y][move_x] = "v"
        move_y += 1
    else:
        return Action.LEFT

def check_obstacle(x, y):
    if BOARD[y][x] == "#":
        return True
    return False

def turn_right():
    x, y = find_guard()
    guard = BOARD[y][x]
    match guard:
        case "<":
            BOARD[y][x] = "^"
        case "^":
            BOARD[y][x] = ">"
        case ">":
            BOARD[y][x] = "v"
        case "v":
            BOARD[y][x] = "<"

def find_guard():
    symbols = {'^', '>', 'v', '<'}
    row_count = 0
    for row in BOARD:
        for i, item in enumerate(row):
            if item in symbols:
                return i, row_count
        row_count += 1

def find_guard_direction():
    x, y = find_guard()
    guard = BOARD[y][x]
    match guard:
        case "<":
            return Direction.LEFT
        case "^":
            return Direction.UP
        case ">":
            return Direction.RIGHT
        case "v":
            return Direction.DOWN

def read_file(path):
    input_arr = []
    with open(path) as file:
        for line in file:
            input_arr.append(list(line.replace("\n", "")))
    return input_arr

if __name__ == "__main__":
    BOARD = read_file(INPUT_PATH)
    print(first_part())
