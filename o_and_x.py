
VBARRIER = '│'
HBARRIER = '─'
CROSSBARRIER = '┼'

EMPTY = ' '
CROSS = 'X'
NOUGHT = 'O'

GRIDH = 3
GRIDW = 3

def get_row_seperator():
    row_seperator = [HBARRIER]*(GRIDW+1) # +1 to also include the labels for the row

    row_seperator = CROSSBARRIER.join(row_seperator) + "\n"
    return row_seperator

def get_header():

    column_labels = range(GRIDW)
    column_labels = [str(label) for label in column_labels] #stringify the labels
    header = f" {VBARRIER}{VBARRIER.join(column_labels)}\n"

    return header

def draw_grid(grid):
    rows = []

    header = get_header()
    rows.append(header)

    for row_num in range(GRIDH):
        rows.append(f"{row_num}{VBARRIER}{VBARRIER.join(grid[row_num])}\n")

    row_seperator = get_row_seperator()
    out = row_seperator.join(rows)

    print(out)

def clear_grid():
    grid = []

    for y in range(GRIDH):
        grid.append([])
        for x in range(GRIDW):
            grid[y].append(EMPTY)

    return grid

def is_valid_coord(number,min_n,max_n):

    try:
        number = int(number)
    except ValueError: #If number is not a valid integer
        return False

    if min_n > number or max_n < number:
        return False
    else:
        return True

def is_empty(x,y,grid):
    if grid[y][x] == EMPTY:
        return True
    else:
        return False

def get_valid_move(grid):
    while True:
        x_coord = input("x: ")
        y_coord = input("y: ")

        #Check if the co-ordinates are valid
        if not is_valid_coord(x_coord,0,GRIDW-1):
            print(f"{x_coord} is not a valid x co-ordinate")
            continue

        elif not is_valid_coord(y_coord,0,GRIDH-1):
            print(f"{y_coord} is not a valid y co-ordinate")
            continue

        else:
            x_coord = int(x_coord)
            y_coord = int(y_coord)

        #Check if the cell is occupied
        if not is_empty(x_coord,y_coord,grid):
            print(f"({x_coord},{y_coord}) is already occupied")
            continue
        else:
            return x_coord, y_coord

def make_move(x_coord,y_coord,turn,grid):
    grid[y_coord][x_coord] = turn
    return grid

def check_columns(grid):

    for col in range(GRIDW):
        has_won = True
        base = grid[0][col]

        for row in range(GRIDH):
            if grid[row][col] != base:
                has_won = False
                break

        if has_won and base != EMPTY:
            return base

    return "" #Return an empty string if no-one has won yet

def check_rows(grid):

    for row in range(GRIDH):
        has_won = True
        base = grid[row][0]

        for col in range(GRIDW):
            if grid[row][col] != base:
                has_won = False
                break

        if has_won and base != EMPTY:
            return base

    return "" #Return an empty string if no-one has won yet

def check_diagonals(grid):
    for x_direction in [1,-1]: #Check both the \ and the / diagonal
        has_won = True

        if x_direction == 1:
            base = grid[0][0]
        elif x_direction == -1:
            base = grid[-1][0]

        for row in grid[::x_direction]:
            for cell in row:
                if cell == base:
                    has_won = False

        if has_won and base != EMPTY:
            return base

    return ""

def check_draw(grid):
    for row in grid:
        for cell in row:
            if cell == EMPTY:
                return ""

    return "Draw"

def check_for_result(grid):
    result = ""

    result = check_columns(grid)

    if not result:
        result = check_rows(grid)

    if not result:
        result = check_diagonals(grid)

    if not result:
        result = check_draw(grid)

    if not result:
        return "No result so far"
    elif result == CROSS:
        return f"{CROSS} wins"
    elif result == NOUGHT:
        return f"{NOUGHT} wins"
    elif result == "Draw":
        return "Draw"

def display_result(grid,result):
    display_turn_seperator()
    draw_grid(grid)
    print()
    print(result)

def display_turn(turn):
    print(f"{turn}'s turn\n")

def display_turn_seperator():
    print('-'*20)

def run_turn(grid, turn):

    display_turn_seperator()
    display_turn(turn)
    draw_grid(grid)

    x_coord, y_coord = get_valid_move(grid)
    grid = make_move(x_coord, y_coord,turn,grid)

    result = check_for_result(grid)

    return grid, result


def play():
    grid = clear_grid()

    result = "No result so far"
    turn = CROSS

    while result == "No result so far":

        grid, result = run_turn(grid, turn)

        if turn == CROSS:
            turn = NOUGHT
        elif turn == NOUGHT:
            turn = CROSS


    display_result(grid,result)


play()
