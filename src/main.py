from days.day3 import Day3


def main():
    day = Day3()
    # file_path = "./puzzles/day3_example.txt"
    file_path = "./puzzles/day3_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
