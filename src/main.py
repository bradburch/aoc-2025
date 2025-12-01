from days.day1 import Day1


def main():
    day = Day1()
    # file_path = "./puzzles/day1_example.txt"
    file_path = "./puzzles/day1_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne(input_data)
    day.partTwo(input_data)


if __name__ == "__main__":
    main()
