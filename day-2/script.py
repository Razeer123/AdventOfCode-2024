INPUT_PATH = "input"

def first_part():
    reports_list = read_file(INPUT_PATH)
    safe_list_count = 0

    for report in reports_list:
        is_safe = 1 if is_increasing(report) or is_decreasing(report) else 0
        safe_list_count += is_safe

    return safe_list_count

def second_part():
    reports_list = read_file(INPUT_PATH)
    safe_list_count = 0

    for report in reports_list:
        is_safe = 1 if is_safe_with_dampener(report) else 0
        safe_list_count += is_safe

    return safe_list_count

def is_increasing(reports):
    return all(x < y and abs(x - y) <= 3 for x, y in zip(reports, reports[1:]))

def is_decreasing(reports):
    return all(x > y and abs(x - y) <= 3 for x, y in zip(reports, reports[1:]))

def is_safe_with_dampener(reports):
    for i in range(len(reports)):
        modified_report = reports[:i] + reports[i + 1:]
        if is_increasing(modified_report) or is_decreasing(modified_report):
            return True
    return False

def read_file(path):
    report_list = []
    with open(path) as file:
        for line in file:
            reports = list(map(int, line.split()))
            report_list.append(reports)
    return report_list

if __name__ == "__main__":
    print(first_part())
    print(second_part())