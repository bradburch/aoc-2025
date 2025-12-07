from days.day7 import Day7


def main():
    day = Day7()
    # file_path = "./puzzles/day7_example.txt"
    file_path = "./puzzles/day7_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
