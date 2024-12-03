def check_trend(arr):
    if all(x < y for x, y in zip(arr, arr[1:])):
        return "increasing"
    elif all(x > y for x, y in zip(arr, arr[1:])):
        return "decreasing"
    else:
        return "other"

def are_differences_between_1_and_3(arr):
    return all(1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))

def is_valid_report(line):
    if check_trend(line) == "other":
        return False
    if not are_differences_between_1_and_3(line):
        return False
    return True

def is_valid_report_if_one_element_is_removed(line):
    for idx_ in range(len(line)):
        new_line = line[:idx_] + line[idx_ + 1:]
        if is_valid_report(new_line):
            return True
    return False

if __name__ == '__main__':
    input_file = '../input.txt'
    with open(input_file, 'r') as f:
        data = f.read().splitlines()

    data = [list(map(int, line.split())) for line in data]

    number_of_valid_reports = 0

    for line in data:
        if is_valid_report(line):
            number_of_valid_reports += 1
        else:
            if is_valid_report_if_one_element_is_removed(line):
                number_of_valid_reports += 1

    print(number_of_valid_reports)
