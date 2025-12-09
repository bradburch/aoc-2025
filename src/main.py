from days.day8 import Day8


def main():
    day = Day8()
    # file_path = "./puzzles/day8_example.txt"
    file_path = "./puzzles/day8_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
