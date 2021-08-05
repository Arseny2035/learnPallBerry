def test(list):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in list:
        if x in numbers:
            numbers.pop(numbers.index(x))
    return len(numbers) == 0

correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def valid_solution(board):
    for x in board:
        if sorted(x) != correct:
            return False

    for y in zip(*board):
        if sorted(y) != correct:
            return False

    for box_x in range(0, 7, 3):
        for box_y in range(0, 7, 3):
            list = []
            for x in range(box_x, box_x + 3):
                for y in range(box_y, box_y + 3):
                    list.append(board[x][y])
            if sorted(list) != correct:
                return False
    return True


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
