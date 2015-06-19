__author__ = 'tracyrohlin'
numbers = {"0": " _ | ||_|   ",
                "1": "     |  |   ",
                "2": " _  _||_    ",
                "3": " _  _| _|   ",
                "4": "   |_|  |   ",
                "5": " _ |_  _|   ",
                "6": " _ |_ |_|   ",
                "7": " _   |  |   ",
                "8": " _ |_||_|   ",
                "9": " _ |_| _|   "}

def check_grid(n):
    for row in n:
        if len(row) != 3:
            raise ValueError("One of the rows is off")
    if len(n) !=4:
        raise ValueError("One of the columns is off")


def grid(ocr):

    top_row = []
    middle_row = []
    last_row = []
    for integer in ocr:
        if integer not in numbers:
            raise ValueError
        top_row.append(numbers[integer][:3])
        middle_row.append(numbers[integer][3:6])
        last_row.append(numbers[integer][6:9])

    top_row = "".join(top_row)
    middle_row = "".join(middle_row)
    last_row = "".join(last_row)
    return [top_row, middle_row, last_row, "".join(" "*3*len(ocr))]

def number(number_list):
    if len(number_list) != 4:
        raise ValueError
    for row in number_list:
        if len(row) < 3:
            raise ValueError
    num_dict = dict((value, key) for key, value in numbers.iteritems())

    digs = []
    for integer in range(0, len(number_list[-1]), 3):
        top_row = number_list[0][integer:integer+3]
        middle_row = number_list[1][integer:integer+3]
        last_row = number_list[2][integer:integer+3]
        spaces = number_list[3][integer:integer+3]
        num = "".join([top_row, middle_row, last_row, spaces])
        digs.append(num)
    result = ""
    for number in digs:
        if number not in num_dict:
            result += "?"
        else:
            result += num_dict[number]

    return result