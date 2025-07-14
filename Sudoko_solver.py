# Sudoku Solver
import tkinter as tk


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def extract_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            val = entries[i][j].get()
            row.append(int(val) if val.isdigit() else 0)
        board.append(row)
    return board


def update_board(board):
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, str(board[i][j]))


def solve():
    board = extract_board()
    if solve_sudoku(board):
        update_board(board)
        status_label.config(text="Solved! 🎉")
    else:
        status_label.config(text="No solution found. ⚠️")


def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
    status_label.config(text="")

# Validation: allow only digits 1–9


def validate_input(P):
    return P.isdigit() and 1 <= int(P) <= 9 if P else True


root = tk.Tk()
root.title("Sudoku Solver 🧩")
entries = [[None for _ in range(9)] for _ in range(9)]

frame = tk.Frame(root)
frame.pack()

vcmd = (root.register(validate_input), '%P')

for i in range(9):
    for j in range(9):
        e = tk.Entry(frame, width=2, font=('Arial', 20),
                     justify='center', validate='key', validatecommand=vcmd)
        e.grid(row=i, column=j, padx=2, pady=2)
        entries[i][j] = e
        if (i // 3 + j // 3) % 2 == 0:
            e.configure(bg="#e0f7fa")

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

solve_button = tk.Button(btn_frame, text="Solve",
                         font=('Arial', 14), command=solve)
solve_button.pack(side='left', padx=10)

clear_button = tk.Button(btn_frame, text="Clear",
                         font=('Arial', 14), command=clear_board)
clear_button.pack(side='right', padx=10)

status_label = tk.Label(root, text="", font=('Arial', 12), fg="blue")
status_label.pack()

root.mainloop()
