import re

INPUT_PATH = "input"
MULTIPLICATION_REGEX = re.compile(r"mul\(\d+,\d+\)")
NUMBERS_REGEX = re.compile(r"\d+")
DISABLE_ENABLED_REGEX = re.compile(r"don't\(\).*?do\(\)", re.DOTALL)
DISABLE_REGEX = re.compile(r"don't\(\).+")

def first_part(computer_memory_input):
    operations = re.findall(MULTIPLICATION_REGEX, computer_memory_input)
    multiplication_sum = 0

    for operation in operations:
        numbers_to_multiply = get_numbers_from_string(operation)
        multiplication_sum += numbers_to_multiply[0] * numbers_to_multiply[1]

    return multiplication_sum

def second_part(computer_memory_input):
    input_without_dont_do = re.sub(DISABLE_ENABLED_REGEX, "", computer_memory_input)
    input_without_dangling_dont = re.sub(DISABLE_REGEX, "", input_without_dont_do)

    return first_part(input_without_dangling_dont)


def get_numbers_from_string(operation):
    numbers = [int(s) for s in re.findall(NUMBERS_REGEX, operation)]
    return numbers

def read_file(path):
    with open(path) as file:
        return file.read().replace('\n', '')

if __name__ == "__main__":
    memory_input = read_file(INPUT_PATH)
    print(first_part(memory_input))
    print(second_part(memory_input))