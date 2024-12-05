INPUT_PATH = "input"
XMAS = "XMAS"
MAS = "MAS"
TILE_SIZE = 3

def first_part(arr):
    return find_xmas_horizontally(arr, False) + find_xmas_horizontally(arr, True) + find_xmas_vertically(arr) + find_xmas_diagonally(arr)

def second_part(arr):
    count = 0
    tiles = split_arr_into_tiles(arr)
    for tile in tiles:
        right_diagonals, left_diagonals = get_diagonals(tile)
        mas_in_right_diagonal = MAS in right_diagonals or MAS[::-1] in right_diagonals
        mas_in_left_diagonal = MAS in left_diagonals or MAS[::-1] in left_diagonals
        count += 1 if mas_in_left_diagonal and mas_in_right_diagonal else 0
    return count

def split_arr_into_tiles(arr):
    tiles = []
    rows, cols = len(arr), len(arr[0])
    for i in range(rows - TILE_SIZE + 1):
        for j in range(cols - TILE_SIZE + 1):
            tile = [row[j:j + TILE_SIZE] for row in arr[i:i + TILE_SIZE]]
            tiles.append(tile)
    return tiles

def find_xmas_horizontally(arr, inversed):
    xmas_count = 0
    xmas_str = XMAS if not inversed else XMAS[::-1]
    for line in arr:
        xmas_count += "".join(line).count(xmas_str)
    return xmas_count

def find_xmas_vertically(arr):
    arr_rotated = list(zip(*arr))[::-1]
    return find_xmas_horizontally(arr_rotated, False) + find_xmas_horizontally(arr_rotated, True)

def get_diagonals(arr):
    n = len(arr)
    right_m = [[''] * i + row + [''] * (n - i - 1) for i, row in enumerate(arr)]
    right_diagonals = [''.join(col) for col in zip(*right_m)]
    left_m = [[''] * i + row[::-1] + [''] * (n - i - 1) for i, row in enumerate(arr)]
    left_diagonals = [''.join(col) for col in zip(*left_m)]
    return right_diagonals, left_diagonals

def find_xmas_diagonally(arr):
    xmas_count = 0
    right_diagonals, left_diagonals = get_diagonals(arr)

    for diagonal in right_diagonals + left_diagonals:
        xmas_count += diagonal.count(XMAS) + diagonal.count(XMAS[::-1])

    return xmas_count

def read_file(path):
    input_arr = []
    with open(path) as file:
        for line in file:
            input_arr.append(list(line.replace("\n", "")))
    return input_arr

if __name__ == "__main__":
    input_array = read_file(INPUT_PATH)
    print(first_part(input_array))
    print(second_part(input_array))
