from days.day6 import Day6


def main():
    day = Day6()
    # file_path = "./puzzles/day6_example.txt"
    file_path = "./puzzles/day6_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines)

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
