class Day7:

    diagram: list[list[str]] = []
    diagram2: list[list[str]] = []
    split: int = 0
    beam_cache: dict = {}

    def parsePuzzleInput(self, input_data: list[str]) -> None:
        for line in input_data:
            self.diagram.append(list(line))
            self.diagram2.append(list(line))

    def partOne(self) -> None:
        start = self.diagram[0].index('S')
        self.helper(start, 1)
        self.printDiagram()

        print("Part One - Total Splits:", self.split)

    def helper(self, start_index: int, start_line: int, counter: int = 0):
        start: int = start_index

        for index, line in enumerate(self.diagram[start_line:]):
            if line[start] == '.':
                line[start] = '|'
            elif line[start] == '|':
                break
            elif line[start] == '^':
                self.split += 1
                if start - 1 >= 0 and index < len(self.diagram):
                    self.helper(start-1, start_line+index, counter + 1)
                if start + 1 < len(line) and index < len(self.diagram):
                    self.helper(start+1, start_line+index, counter + 1)
                break

    def helper2(self, row: int, col: int) -> int:
        if col < 0 or col > len(self.diagram2[0]):
            return 0
        if row == len(self.diagram2):
            return 1
        if (row, col) in self.beam_cache:
            return self.beam_cache[(row, col)]
        result = -1
        if self.diagram2[row][col] == '^':
            result = self.helper2(row+1, col-1) + self.helper2(row+1, col+1)
        else:
            result = self.helper2(row+1, col)
        self.beam_cache[(row, col)] = result
        return result

    def partTwo(self) -> None:
        total: int = 0

        start = self.diagram2[0].index('S')

        total = self.helper2(1, start)

        print("Part Two - Correct Totals:", total)

    def printDiagram(self) -> None:
        for line in self.diagram:
            print("".join(line))
        print('---------------------')
