import csv

row1 = list()
row2 = list()
row3 = list()
row4 = list()
row5 = list()
row6 = list()
row7 = list()


def main():
    csv_file = csv.reader(open('C:\\Users\\Rohit\\Downloads\\HIER.csv', 'r'))
    count = 0
    for row in csv_file:
        initialize_array(row, count)
        count = count + 1
        # print(row)
    print(row1)
    print(row2)
    print(row3)
    print(row4)
    print(row5)
    print(row6)
    print(row7)
    # print(distance.euclidean([9.2, 9.3, 0], [2.4, 2.5, 0], [8.9, 8.7, 0]))


def initialize_array(row, count):
    if count == 1:
        global row1
        row1 = extract_data(row)
    elif count == 2:
        global row2
        row2 = extract_data(row)
    elif count == 3:
        global row3
        row3 = extract_data(row)
    elif count == 4:
        global row4
        row4 = extract_data(row)
    elif count == 5:
        global row5
        row5 = extract_data(row)
    elif count == 6:
        global row6
        row6 = extract_data(row)
    elif count == 7:
        global row7
        row7 = extract_data(row)


def extract_data(row):
    count = 0
    al = list()
    for f in row:
        if count > 0:
            al.append(float(f))
        count = count + 1
    del al[0]
    return al


if __name__ == '__main__':
    main()
