import random
import copy


# sudoku board

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


# print the board to terminal

def print_board(board):
    print("\n  1 2 3   4 5 6   7 8 9")
    for i, row in enumerate(board):
        if i % 3 == 0:
            print(" +-------+-------+-------+")
        print(f"{i+1}|", end=" ")
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else ".", end=" ")
        print("|")
    print(" +-------+-------+-------+")


# get all numbers that can go in a cell without breaking the rules

def get_options(board, r, c):
    if board[r][c] != 0:
        return set()

    options = set(range(1, 10))
    options -= set(board[r])
    options -= {board[i][c] for i in range(9)}

    br, bc = (r // 3) * 3, (c // 3) * 3
    options -= {board[i][j] for i in range(br, br+3) for j in range(bc, bc+3)}

    return options

# fill in cells that only have one possible number, repeat until nothing changes

def fill_obvious(board):
    board = copy.deepcopy(board)
    changed = True
    while changed:
        changed = False
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    opts = get_options(board, r, c)
                    if len(opts) == 1:
                        board[r][c] = opts.pop()
                        changed = True
    return board


# count how many conflicts are in the board (lower is better)

def count_conflicts(board):
    total = 0
    for i in range(9):
        total += 9 - len(set(board[i]))
        total += 9 - len(set(board[r][i] for r in range(9)))

    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = []
            for r in range(br, br+3):
                for c in range(bc, bc+3):
                    box.append(board[r][c])
            total += 9 - len(set(box))
    return total

# make a random board where each row has all numbers 1-9

def make_random_board(board):
    candidate = copy.deepcopy(board)
    for r in range(9):
        missing = list(set(range(1, 10)) - set(candidate[r]))
        random.shuffle(missing)
        for c in range(9):
            if candidate[r][c] == 0:
                candidate[r][c] = missing.pop()
    return candidate

# swap two random cells in a row (only non-fixed cells)

def swap_cells(board, original):
    r = random.randint(0, 8)
    free_cols = [c for c in range(9) if original[r][c] == 0]
    if len(free_cols) >= 2:
        c1, c2 = random.sample(free_cols, 2)
        board[r][c1], board[r][c2] = board[r][c2], board[r][c1]

# keep generating and tweaking random boards until we find one with no conflicts

def solve_with_ai(board, max_rounds=1000, pool_size=200):
    original = copy.deepcopy(board)
    pool = [make_random_board(board) for _ in range(pool_size)]

    for round in range(max_rounds):
        pool.sort(key=count_conflicts)
        if count_conflicts(pool[0]) == 0:
            return pool[0]

        next_pool = pool[:20]
        while len(next_pool) < pool_size:
            picked = random.choice(pool[:50])
            new_board = copy.deepcopy(picked)
            swap_cells(new_board, original)
            next_pool.append(new_board)
        pool = next_pool

    return pool[0]


# check if every cell is filled

def is_done(board):
    return all(all(cell != 0 for cell in row) for row in board)

def main():
    board = copy.deepcopy(sudoku_board)

    while True:
        print_board(board)

        print("1. Enter a number")
        print("2. Auto solve")
        print("3. Quit")

        choice = input("Choose (1/2/3): ")

        if choice == "1":
            move = input("Enter: row col num (example: 1 3 2): ")

            try:
                r, c, n = map(int, move.split())
                r -= 1
                c -= 1

                if board[r][c] != 0:
                    print("Can't change a starting number")
                    continue

                if n not in get_options(board, r, c):
                    print("That number breaks the rules")
                    continue

                board[r][c] = n

                if is_done(board) and count_conflicts(board) == 0:
                    print_board(board)
                    print("Nice, you solved it!")
                    break

            except ValueError:
                print("Wrong format! Example: 1 3 9")
            except IndexError:
                print("Row and column must be between 1 and 9")

        elif choice == "2":
            board = fill_obvious(board)
            board = solve_with_ai(board)
            print_board(board)
            print("Solved by AI")
            break

        elif choice == "3":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()