input_file = '../input.txt'

if __name__ == '__main__':
    with open(input_file, 'r') as f:
        data = f.read().splitlines()

    data = [list(map(int, line.split())) for line in data]

    number_of_valid_reports = 0

    for line in data:
        increasing = line[0] - line[1] < 0
        good_report = True
        for idx in range(0, len(line) - 1):
            difference = line[idx] - line[idx + 1]
            if abs(difference) < 1 or abs(difference) > 3:
                good_report = False
                break
            if increasing and difference > 0:
                good_report = False
                break
            if not increasing and difference < 0:
                good_report = False
                break
        if good_report:
            number_of_valid_reports += 1

    print(number_of_valid_reports)
