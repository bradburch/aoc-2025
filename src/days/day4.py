class Day4:

    grid = []

    def parsePuzzleInput(self, input_data: list[str]) -> None:
        for line in input_data:
            self.grid.append(line)

    def partOne(self) -> None:
        paper_rolls: int = 0

        for y, row in enumerate(self.grid):
            x: int = row.index('@')

            while x < len(row):
                try:
                    if self.checkSurroundings(y, x):
                        paper_rolls += 1
                    next_roll: int = row.index('@', x+1)
                    x = next_roll
                except Exception as e:
                    break

        print("Part One - Paper Towel Rolls Available:", paper_rolls)

    def checkSurroundings(self, y: int, x: int, partTwo: bool = False) -> bool:
        rolls: int = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                nY: int = y + i
                nX: int = x + j
                if nY == y and nX == x:
                    continue
                if nY >= 0 and nY < len(self.grid) and nX < len(self.grid[nY]) and nX >= 0:
                    if self.grid[nY][nX] == '@':
                        rolls += 1

        if rolls < 4:
            return True
        else:
            return False

    def partTwo(self) -> None:
        paper_rolls: int = 0
        added: bool = True
        remove: set[Coords] = set()

        while added:
            for y, row in enumerate(self.grid):
                try:
                    x: int = row.index('@')
                except:
                    continue

                while x < len(row):
                    try:
                        if self.checkSurroundings(y, x):
                            paper_rolls += 1
                            remove.add(Coords(y, x))
                        next_roll: int = row.index('@', x+1)
                        x = next_roll
                    except Exception as e:
                        break

            if len(remove) == 0:
                break

            for rem in remove:
                row: str = self.grid[rem.y]
                rem_row: str = row[:rem.x] + '.' + row[rem.x + 1:]
                self.grid[rem.y] = rem_row

            remove.clear()

        print("Part Two - All Rolls Removed:", paper_rolls)


class Coords:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
