class Day1:

    def parsePuzzleInput(self, input_data: list[str]):
        pass

    def partOne(self, input_data):
        starting_value = 50
        counter = 0

        for line in input_data:
            direction = line[0]
            turns = int(line[1:])

            if direction == "L":
                turns *= -1

            temp_position = starting_value + turns
            starting_value = temp_position % 100

            if starting_value == 0:
                counter += 1

        print("Part One - Times at Zero:", counter)

    def partTwo(self, input_data):
        starting_value = 50
        counter = 0

        for line in input_data:
            direction = line[0]
            turns = int(line[1:])

            if direction == "R":
                distance_to_zero = (100 - starting_value) % 100
            else:
                distance_to_zero = starting_value

            if distance_to_zero == 0:
                distance_to_zero = 100

            if turns >= distance_to_zero:
                counter += (turns - distance_to_zero) // 100
                counter += 1

            if direction == "L":
                turns = turns * -1

            temp_position = starting_value + turns
            starting_value = temp_position % 100

        print("Part Two - Times past Zero:", counter)
