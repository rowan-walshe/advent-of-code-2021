from typing import List


class BingoBoard():
    def __init__(self, board: List[List[int]]):
        self._board = board
        self._hit = [[False for i in range(5)] for i in range(5)]
        self._complete = False

    def isComplete(self) -> bool:
        # Return cached True
        if self._complete:
            return True
        # Check horizontal
        for i in self._hit:
            if all(i):
                self._complete = True
                return True
        # Check vertical
        for i in range(len(self._hit)):
            self._complete = True
            for j in range(len(self._hit)):
                if not self._hit[j][i]:
                    self._complete = False
                    continue
            if self._complete:
                return True
        # Check diagonals
        self._complete = all([self._hit[i][i] for i in range(len(self._hit))])
        self._complete = self._complete or \
            all([self._hit[i][len(self._hit) - 1 - i]
                 for i in range(len(self._hit))])
        return self._complete

    def evalNumber(self, n: int):
        for i in range(len(self._board)):
            for j in range(len(self._board)):
                if self._board[i][j] == n:
                    self._hit[i][j] = True

    def getUnhitNumbers(self) -> List[int]:
        res = []
        for i in range(len(self._hit)):
            for j in range(len(self._hit)):
                if not self._hit[i][j]:
                    res.append(self._board[i][j])
        return res

    def __str__(self):
        res = ""
        for i in self._board:
            for j in i:
                res += str(j).rjust(2).ljust(3)
            res += '\n'
        return res


def part1(numbers: List[int], bingo_boards: List[BingoBoard]) -> int:
    for n in numbers:
        for board in bingo_boards:
            board.evalNumber(n)
            if board.isComplete():
                return sum(board.getUnhitNumbers()) * n
    raise Exception("Didn't find a winning bingo board")


def part2(numbers: List[int], bingo_boards: List[BingoBoard]) -> int:
    remaining = len(bingo_boards)
    for n in numbers:
        for board in bingo_boards:
            if board.isComplete():
                continue
            board.evalNumber(n)
            if board.isComplete():
                remaining -= 1
            if remaining == 0:
                return sum(board.getUnhitNumbers()) * n
    raise Exception("Didn't find a winning bingo board")


if __name__ == "__main__":
    with open("input", 'r') as f:
        lines = f.readlines()
    calling_numbers = list(map(int, lines[0].strip().split(',')))
    board_numbers = list(map(lambda x: list(map(int, x.strip().split())),
                             lines[2:]))
    bingo_boards_1 = []
    for i in range(0, len(board_numbers), 6):
        bingo_boards_1.append(BingoBoard(board_numbers[i:i+5]))
    bingo_boards_2 = []
    for i in range(0, len(board_numbers), 6):
        bingo_boards_2.append(BingoBoard(board_numbers[i:i+5]))

    print(f"part1: {part1(calling_numbers, bingo_boards_1)}")
    print(f"part2: {part2(calling_numbers, bingo_boards_2)}")
