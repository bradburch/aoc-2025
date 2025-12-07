import re
import math


class Day6:

    problems: list[list[int]] = []
    operators: list[str] = []

    input_text: list[str] = []

    def parsePuzzleInput(self, input_data: list[str]) -> None:
        self.input_text = input_data
        for line in input_data:
            cols = re.split(r'[\s]+', line.strip())

            for i, c in enumerate(cols):
                if not i < len(self.problems):
                    self.problems.append([])

                if c.isdigit():
                    self.problems[i].append(int(c))
                else:
                    self.operators.append(c)

    def partOne(self) -> None:
        total: int = 0

        for index, problem in enumerate(self.problems):
            if self.operators[index] == '+':
                total += sum(problem)
            else:
                total += math.prod(problem)

        print("Part One - Total Normal:", total)

    def partTwo(self) -> None:
        total: int = 0

        op_indicies = [i for i, val in enumerate(
            self.input_text[-1][::-1]) if val == '*' or val == '+']
        first = self.input_text[0][::-1]
        second = self.input_text[1][::-1]
        third = self.input_text[2][::-1]
        fourth = self.input_text[3][::-1]
        rev_operators = self.operators[::-1]

        start = 1

        for ind, index in enumerate(op_indicies):
            f_num = first[start: index+2]
            s_num = second[start: index+2]
            t_num = third[start: index+2]
            fo_num = fourth[start: index+2]

            problem = []
            for i, c in enumerate(f_num):
                problem.append(c)

            for i, c in enumerate(s_num):
                problem[i] = problem[i] + c

            for i, c in enumerate(t_num):
                problem[i] = problem[i] + c

            for i, c in enumerate(fo_num):
                problem[i] = problem[i] + c

            prob_nums = list(map(int, problem))

            if rev_operators[ind] == '+':
                total += sum(prob_nums)
            else:
                total += math.prod(prob_nums)

            start = index + 3

        print("Part Two - Correct Totals:", total)
