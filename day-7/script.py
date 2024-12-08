from enum import Enum
import itertools

INPUT_PATH = "input"

class Operations(Enum):
    ADDITION = 1,
    MULTIPLICATION = 2,
    COMBINATION = 3

def first_part(is_combination_on = False):
    equations = read_file(INPUT_PATH)
    all_valid_operations_sum = 0

    for equation in equations:
        result, numbers = parse_line(equation)
        operations_permutations = generate_operations_permutations(len(numbers) - 1)
        all_valid_operations_sum += apply_operations(result, numbers, operations_permutations, is_combination_on)

    return all_valid_operations_sum

def second_part():
    return first_part(True)

def apply_operations(wanted_result, numbers, operations_permutations, is_combination_on):
    for permutation in operations_permutations:
        result = numbers[0]

        for i in range(0, len(numbers) - 1):
            if permutation[i] is Operations.ADDITION:
                result += numbers[i + 1]
            elif permutation[i] is Operations.MULTIPLICATION:
                result *= numbers[i + 1]
            elif is_combination_on and permutation[i] is Operations.COMBINATION:
                result = int(str(result) + str(numbers[i + 1]))

        if result == wanted_result:
            return wanted_result

    return 0

def generate_operations_permutations(times):
    return list(itertools.product([Operations.ADDITION, Operations.MULTIPLICATION, Operations.COMBINATION], repeat=times))

def parse_line(line):
    sides_of_equation = line.split(": ")
    return int(sides_of_equation[0]), [int(x) for x in sides_of_equation[1].split()]

def read_file(path):
    input_arr = []
    with open(path) as file:
        for line in file:
            input_arr.append(line.replace("\n", ""))
    return input_arr

if __name__ == "__main__":
    print(first_part())
    print(second_part())
