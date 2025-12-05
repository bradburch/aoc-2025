class Day5:

    fresh_range: list[list[int]] = []
    check_ids: list[int] = []
    union_ranges: list[list[int]] = []

    def parsePuzzleInput(self, input_data: list[str]) -> None:
        fresh_ranges = True
        for line in input_data:
            if not line:
                fresh_ranges = False
                continue

            if fresh_ranges:
                parts = line.split('-')

                self.fresh_range.append([int(parts[0]), int(parts[1])])
            else:
                self.check_ids.append(int(line))

        self.union()

    def union(self) -> None:
        for begin, end in sorted(self.fresh_range, key=lambda x: x[0]):
            if self.union_ranges and self.union_ranges[-1][1] >= begin - 1:
                self.union_ranges[-1][1] = max(self.union_ranges[-1][1], end)
            else:
                self.union_ranges.append([begin, end])

    def partOne(self) -> None:
        fresh: int = 0

        for id in self.check_ids:
            for begin, end in self.union_ranges:
                if id >= begin and id <= end:
                    fresh += 1

        print("Part One - Fresh Produce:", fresh)

    def partTwo(self) -> None:
        fresh: int = 0

        for begin, end in self.union_ranges:
            valid: int = end - begin + 1
            fresh += valid

        print("Part Two - All Fresh Produce:", fresh)
