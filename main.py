import csv
import math

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
    r1 = [0.0]*7
    print(r1)

    r2 = [get_distance(row1, row2), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    print(r2)

    r3 = [get_distance(row1, row3), get_distance(row2, row3), 0.0, 0.0, 0.0, 0.0, 0.0]
    print(r3)

    r4 = [get_distance(row1, row4), get_distance(row2, row4), get_distance(row3, row4), 0.0, 0.0, 0.0, 0.0]
    print(r4)

    r5 = [get_distance(row1, row5), get_distance(row2, row5), get_distance(row3, row5), get_distance(row4, row5), 0.0,
          0.0, 0.0]
    print(r5)

    r6 = [get_distance(row1, row6), get_distance(row2, row6), get_distance(row3, row6), get_distance(row4, row6),
          get_distance(row5, row6), 0.0, 0.0]
    print(r6)

    r7 = [get_distance(row1, row7), get_distance(row2, row7), get_distance(row3, row7), get_distance(row4, row7),
          get_distance(row5, row7), get_distance(row6, row7), 0.0]
    print(r7)


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
    #del al[0]
    return al


def get_distance(l1, l2):
    r = math.sqrt(math.pow(l1[0]-l2[0], 2) + math.pow(l1[1] - l2[1], 2) + math.pow(l1[2] - l2[2], 2) + math.pow(l1[3] - l2[3], 2) +
                  math.pow(l1[4] - l2[4], 2) + math.pow(l1[5] - l2[5], 2))
    return r


if __name__ == '__main__':
    main()
