#!/usr/bin/python3
from sys import argv
from sys import exit

def error_exit(message=""):
    """prints message to the terminal and exits
    Args:
        message (str): message to print
    """
    print("{}".format(message), end="\n")
    exit(1)



def back_track(r):
    if r == n:
        copy = []
        for y, row in enumerate(board):
            inner = []
            for x, cell in enumerate(row):
                if cell == "Q":
                    inner.append(y)
                    inner.append(x)
            copy.append(inner)
        res.append(copy)
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = "Q"
        
        back_track(r + 1)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = "."

if __name__ == "__main__":
    if len(argv) != 2:
        error_exit("Usage: nqueens N")
    elif not isinstance()
    