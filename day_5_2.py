from utils import parse_input

def get_row(entry):
    row_letters = entry[:7]
    min_row, max_row = 0, 127
    for letter in row_letters:
        if letter == "F":
            max_row = min_row + (max_row - min_row + 1)/2 - 1
        else:
            min_row = max_row - (max_row - min_row + 1)/2 + 1
    return min_row

def get_column(entry):
    column_letters = entry[7:]
    min_column, max_column = 0, 7
    for letter in column_letters:
        if letter == "L":
            max_column = min_column + (max_column - min_column + 1)/2 - 1
        else:
            min_column = max_column - (max_column - min_column + 1)/2 + 1
            
    return min_column

def get_seat_id(row, column):
    return row*8 + column

def get_empty_seat(boarding_pass_seats):
    all_possible_seats = range(0, 1025)
    empty_seats = [seat for seat in all_possible_seats if seat not in boarding_pass_seats]
    for seat in empty_seats:
        if seat-1 in boarding_pass_seats and seat+1 in boarding_pass_seats:
            return seat

inputs = parse_input("inputs/day_5.txt")

boarding_pass_seats = [get_seat_id(get_row(entry), get_column(entry)) for entry in inputs]

print(get_empty_seat(boarding_pass_seats))