class Day3:

    banks: list[str] = []

    def parsePuzzleInput(self, input_data: list[str]) -> None:
        self.banks = input_data

    def partOne(self) -> None:
        joltage = 0

        for batteries in self.banks:
            highest = max(batteries)
            highest_index = batteries.index(highest)
            second_highest = 0

            if highest_index == len(batteries) - 1:
                second_highest = highest
                highest = max(batteries[:highest_index])
            else:
                batteries_after = batteries[highest_index + 1:]
                second_highest = max(batteries_after)

            j_str = highest + second_highest
            joltage += int(j_str)

        print("Part One - Largest 2 Battery Bank Joltage:", joltage)

    def partTwo(self) -> None:
        joltage = 0

        for batteries in self.banks:
            switched_on = ""
            start_index = 0
            for i in range(11, -1, -1):
                available_batteries = batteries[start_index:len(batteries)-i]
                highest = max(available_batteries)
                highest_index = available_batteries.index(highest)
                switched_on += highest
                start_index += highest_index + 1

            joltage += int(switched_on)

        print("Part Two - Largest 12 Battery Bank Joltage:", joltage)
