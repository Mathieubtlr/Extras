# connect_four.py

import numpy as np

### Possible improvement: create a function that recognizes a double attack pattern

# Summary of improvements made:
#   - Alpha-beta pruning (to understand)
#   - Do not try to align 3 or 2 in a column when touching the ceiling, same for rows
#   - Depth increases by 1 every 10 moves, after 30 moves depth is 9
#

# player = 1 or -1
def init():
    return np.zeros((6, 7))

def is_full(grid, col):
    return all(grid[row][col] == 1 or grid[row][col] == -1 for row in range(6))

def play_move(grid, col, player):  # col = column index
    assert not is_full(grid, col)
    row = 5
    not_placed = True
    while row > -1 and not_placed:
        if grid[row][col] == 0:
            grid[row][col] = player
            not_placed = False
        else:
            row -= 1

def undo_move(grid, col):  # remove the last piece in the column
    row = 0
    not_taken_back = True
    while row < 6 and not_taken_back:
        if grid[row][col] != 0:
            grid[row][col] = 0
            not_taken_back = False
        else:
            row += 1

def win_row(grid, player):
    for i in range(6):
        for j in range(4):
            if all(player == grid[i][j + k] for k in range(4)):
                return True
    return False

def win_col(grid, player):
    for j in range(7):
        for i in range(3):
            if all(player == grid[i + k][j] for k in range(4)):
                return True
    return False

def win_diag(grid, player):
    for i in range(6):
        for j in range(7):
            if (i + 3) <= 5 and (j + 3) <= 6:
                if all(player == grid[i + k][j + k] for k in range(4)):
                    return True
    return False

def win_anti_diag(grid, player):
    for i in range(6):
        for j in range(7):
            if i + 3 <= 5 and j - 3 >= 0:
                if all(player == grid[i + k][j - k] for k in range(4)):
                    return True
    return False

def win(grid, player):
    return win_row(grid, player) or win_col(grid, player) or win_diag(grid, player) or win_anti_diag(grid, player)

def draw(grid):
    return not (0 in grid)

def end(grid):
    return win(grid, 1) or win(grid, -1) or draw(grid)

def computer_move(grid, depth, computer_id):  # computer_id = AI’s player value, depth = search depth
    best_score = -np.inf
    best_move = None
    for j in [3, 4, 2, 5, 1, 6, 0]:  # this order performs better with pruning
        if not is_full(grid, j):
            play_move(grid, j, computer_id)
            score = minimax(grid, -1 * computer_id, 1, depth, computer_id, -np.inf, np.inf)
            print(j, score)
            undo_move(grid, j)
            if score > best_score:
                best_score = score
                best_move = j
    column = best_move
    play_move(grid, column, computer_id)
    print("Computer plays in column:", column)

# Around 20s per move for depth = 6 (≈33,000 operations)
count = 0

def minimax(grid, player, current_depth, max_depth, computer_id, alpha, beta):
    global count
    count += 1
    # if count % 1000 == 0:
    #     print(count)
    if current_depth == max_depth or end(grid):
        return heuristic(grid, computer_id)

    if player == computer_id:
        best_score = -np.inf
        for j in [3, 4, 2, 5, 1, 6, 0]:
            if not is_full(grid, j):
                play_move(grid, j, computer_id)
                score = minimax(grid, -1 * player, current_depth + 1, max_depth, computer_id, alpha, beta)
                undo_move(grid, j)
                if score > best_score:
                    best_score = score
                if score > beta:
                    return score
                alpha = max(alpha, score)
        return best_score

    else:  # opponent’s turn
        best_score = np.inf
        for j in [3, 4, 2, 5, 1, 6, 0]:
            if not is_full(grid, j):
                play_move(grid, j, -1 * computer_id)
                score = minimax(grid, -1 * player, current_depth + 1, max_depth, computer_id, alpha, beta)
                undo_move(grid, j)
                if score < best_score:
                    best_score = score
                if score < alpha:
                    return score
                beta = min(beta, score)
        return best_score

def play_vs_computer(depth, computer_id):  # if the computer starts, computer_id = 1; else -1
    grid = init()
    player = 1
    while not end(grid):
        if progress(grid) > 5:
            depth = 7
        if progress(grid) > 20:
            depth = 8
        if progress(grid) > 22:
            depth = 9
        if progress(grid) > 23:
            depth = 10
        if progress(grid) > 24:
            depth = 11
        if progress(grid) > 25:
            depth = 12
        if progress(grid) > 26:
            depth = 13
        if progress(grid) > 27:
            depth = 14

        if player == -1 * computer_id:
            col = int(input("Column: "))
            play_move(grid, col, player)
            print(grid)
            if win(grid, player):
                return "Player " + str(player) + " wins"
            elif draw(grid):
                return "Draw"
            player = -1 * player
        elif player == computer_id:
            computer_move(grid, int(depth), computer_id)
            print(grid)
            if win(grid, player):
                return "Player " + str(player) + " wins"
            elif draw(grid):
                return "Draw"
            player = -1 * player

def play_computers(depth1, depth2):
    grid = init()
    player = 1
    while not end(grid):
        depth1 += 0.1
        depth2 += 0.1
        if player == 1:
            computer_move(grid, int(depth1), 1)
            print(grid)
            if win(grid, player):
                return "Player " + str(player) + " wins"
            elif draw(grid):
                return "Draw"
            player = -1 * player
        elif player == -1:
            computer_move(grid, int(depth2), -1)
            print(grid)
            if win(grid, player):
                return "Player " + str(player) + " wins"
            elif draw(grid):
                return "Draw"
            player = -1 * player

def count_open_rows(grid, player):
    c = 0
    for i in range(6):
        for j in range(4):
            if all(grid[i][j + k] != -1 * player for k in range(4)):
                c += 1
    return c

def count_open_cols(grid, player):
    c = 0
    for j in range(7):
        for i in range(3):
            if all(grid[i + k][j] != -1 * player for k in range(4)):
                c += 1
    return c

def count_open_diag(grid, player):
    c = 0
    for i in range(6):
        for j in range(7):
            if (i + 3) <= 5 and (j + 3) <= 6:
                if all(grid[i + k][j + k] != -1 * player for k in range(4)):
                    c += 1
    return c

def count_open_anti_diag(grid, player):
    c = 0
    for i in range(6):
        for j in range(7):
            if (i + 3) <= 5 and (j - 3) >= 0:
                if all(grid[i + k][j - k] != -1 * player for k in range(4)):
                    c += 1
    return c

def win3_row(grid, player):
    for i in range(6):
        for j in [1, 2, 3]:
            if all(player == grid[i][j + k] for k in range(3)):
                return True
    return False

def win3_col(grid, player):
    for j in range(7):
        for i in [1, 2, 3]:
            if all(player == grid[i + k][j] for k in range(3)):
                return True
    return False

def win3_diag(grid, player):
    for i in range(6):
        for j in range(7):
            if (i + 2) <= 5 and (j + 2) <= 6:
                if all(player == grid[i + k][j + k] for k in range(3)):
                    return True
    return False

def win3_anti_diag(grid, player):
    for i in range(6):
        for j in range(7):
            if i + 2 <= 5 and j - 2 >= 0:
                if all(player == grid[i + k][j - k] for k in range(3)):
                    return True
    return False

def win3(grid, player):
    return win3_row(grid, player) or win3_col(grid, player) or win3_diag(grid, player) or win3_anti_diag(grid, player)

def win2_row(grid, player):
    for i in range(6):
        for j in [1, 2, 3, 4]:
            if all(player == grid[i][j + k] for k in range(2)):
                return True
    return False

def win2_col(grid, player):
    for j in range(7):
        for i in [1, 2, 3, 4]:
            if all(player == grid[i + k][j] for k in range(2)):
                return True
    return False

def win2_diag(grid, player):
    for i in range(6):
        for j in range(7):
            if (i + 1) <= 5 and (j + 2) <= 6:
                if all(player == grid[i + k][j + k] for k in range(2)):
                    return True
    return False

def win2_anti_diag(grid, player):
    for i in range(6):
        for j in range(7):
            if i + 1 <= 5 and j - 2 >= 0:
                if all(player == grid[i + k][j - k] for k in range(2)):
                    return True
    return False

def win2(grid, player):
    return win2_row(grid, player) or win2_col(grid, player) or win2_diag(grid, player) or win2_anti_diag(grid, player)

def heuristic(grid, player):
    A = count_open_rows(grid, player) + count_open_cols(grid, player) + count_open_diag(grid, player) + count_open_anti_diag(grid, player)
    if win(grid, player):
        A += 30
    if win3(grid, player):
        A += 10
    if win2(grid, player):
        A += 5
    player = -1 * player
    B = count_open_rows(grid, player) + count_open_cols(grid, player) + count_open_diag(grid, player) + count_open_anti_diag(grid, player)
    if win(grid, player):
        B += 30
    if win3(grid, player):
        B += 10
    if win2(grid, player):
        B += 5
    return A - B

def progress(grid):
    count = 0
    for i in range(6):
        for j in range(7):
            if grid[i][j] != 0:
                count += 1
    return count

def double_attack(grid, player):  # special pattern recognition
    for i in range(1, 6):
        for j in range(7):
            if i + 2 <= 5 and j + 2 <= 6:
                if grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 2][j] == grid[i + 2][j + 1] == player:
                    return True
    return False


play_vs_computer(5, 1)
