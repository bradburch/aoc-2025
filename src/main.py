from days.day5 import Day5


def main():
    day = Day5()
    file_path = "./puzzles/day5_example.txt"
    # file_path = "./puzzles/day5_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
