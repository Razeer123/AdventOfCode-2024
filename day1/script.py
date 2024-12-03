INPUT_PATH = "input"

def first_part():
    list1, list2 = read_file(INPUT_PATH)

    list1.sort()
    list2.sort()

    difference_sum = 0

    for i in range(len(list1)):
        difference_sum += abs(list1[i] - list2[i])

    return difference_sum

def second_part():
    list1, list2 = read_file(INPUT_PATH)
    occurrences = {}
    similarity_score = 0

    for i in range(len(list1)):
        current_value = list1[i]
        occurrences_time = occurrences[current_value] if current_value in occurrences else None
        if occurrences_time is None:
            occurrences_time = list2.count(current_value)
            occurrences[current_value] = occurrences_time
        similarity_score += list1[i] * occurrences_time

    return similarity_score

def read_file(path):
    list1, list2 = [], []
    with open(path) as file:
        for line in file:
            col1, col2 = map(int, line.split())
            list1.append(col1)
            list2.append(col2)
    return list1, list2

if __name__ == "__main__":
    print(first_part())
    print(second_part())