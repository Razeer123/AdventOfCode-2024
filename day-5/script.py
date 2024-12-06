from collections import defaultdict

INPUT_PATH = "input"
RULES_PATH = "rules"

def first_and_second_part(rules, updates):
    middle_sum_correct = 0
    middle_sum_incorrect = 0
    for update in updates:
        numbers = update.split(",")
        order_correct = True

        for number in numbers:
            elements_that_cant_be_before = rules[number]
            number_index = update.find(number)
            elements_indexes = [update.find(elem) for elem in elements_that_cant_be_before if update.find(elem) != -1]

            if all(number_index < index for index in elements_indexes):
                continue
            else:
                order_correct = False
                break

        if order_correct:
            middle_sum_correct += int(numbers[len(numbers) // 2])

        # Topological sort
        if order_correct is False:
            graph = defaultdict(list)
            in_degree = defaultdict(int)

            # Create map of dependencies -> we'll know which value goes first
            # We'll then find next 'unblocked' number and repeat
            for num in numbers:
                for forbidden in rules[num]:
                    if forbidden in numbers:
                        graph[forbidden].append(num)
                        in_degree[num] += 1

            sorted_numbers = []
            zero_in_degree = [num for num in numbers if in_degree[num] == 0]

            while zero_in_degree:
                current = zero_in_degree.pop(0)
                sorted_numbers.append(current)
                for neighbor in graph[current]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        zero_in_degree.append(neighbor)

            middle_sum_incorrect += int(sorted_numbers[len(sorted_numbers) // 2])

    return middle_sum_correct, middle_sum_incorrect
def parse_rules(rules):
    prev_next_map = defaultdict(list)
    for rule in rules:
        curr_rule = rule.split("|")
        prev_next_map[curr_rule[0]].append(curr_rule[1])
    return prev_next_map

def read_file(path):
    lines = []
    with open(path) as file:
        for line in file:
            lines.append(line.replace("\n", ""))
    return lines

if __name__ == "__main__":
    update_list = read_file(INPUT_PATH)
    rules_list = parse_rules(read_file(RULES_PATH))
    print(first_and_second_part(rules_list, update_list))
