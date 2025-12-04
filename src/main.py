from days.day4 import Day4


def main():
    day = Day4()
    # file_path = "./puzzles/day4_example.txt"
    file_path = "./puzzles/day4_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
