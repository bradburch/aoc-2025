from days.day2 import Day2


def main():
    day = Day2()
    # file_path = "./puzzles/day2_example.txt"
    file_path = "./puzzles/day2_puzzle.txt"
    input_data = []
    with open(file_path, "r") as file:
        for lines in file:
            input_data.append(lines.strip())

    day.parsePuzzleInput(input_data)
    day.partOne()
    day.partTwo()


if __name__ == "__main__":
    main()
