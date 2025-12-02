from collections import Counter
import re


class Day2:

    ranges: list[Range] = []

    def parsePuzzleInput(self, input_data: list[str]):
        ran = input_data[0].split(",")
        for r in ran:
            parts = r.split("-")
            self.ranges.append(Range(int(parts[0]), int(parts[1])))

    def partOne(self):
        invalids = 0

        for r in self.ranges:
            for i in range(r.start, r.end + 1):
                i_length = len(str(i))
                if i_length % 2 == 0:
                    half = i_length // 2
                    first_half = str(i)[:half]
                    second_half = str(i)[half:]
                    if first_half == second_half:
                        invalids += i

        print("Part One - Number of One Repeats:", invalids)

    def partTwo(self):
        invalids = 0

        for r in self.ranges:
            for i in range(r.start, r.end + 1):
                pattern = r"^(.+?)(?:\1)+$"
                match = re.match(pattern, str(i))
                if match:
                    invalids += i
                    continue

        print("Part Two - Number of All Repeats:", invalids)


class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
