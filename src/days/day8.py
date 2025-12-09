import math


class Day8:

    boxes: list[list[int]] = []
    dist_map: dict = {}

    def parsePuzzleInput(self, input_data: list[str]) -> None:
        for line in input_data:
            self.boxes.append(list(map(int, line.split(','))))

    def partOne(self) -> None:
        total: int = 1

        for fi, box in enumerate(self.boxes):
            for si, b in enumerate(self.boxes[:fi+1]):
                d = math.dist(box, b)
                self.dist_map[d] = (fi, si)

        sorted_map = dict(sorted(self.dist_map.items())[:1000])
        circuits: list[set[int]] = []

        for v in sorted_map.values():
            circuits = self.connect(v[0], v[1], circuits)

        sorted_circuits = sorted(circuits, key=len, reverse=True)

        largest = sorted_circuits[:3]

        for l in largest:
            total *= len(l)

        print("Part One - Length of Largest:", total)

    def findCircuit(self, box: int, circuits: list[set[int]]) -> int:
        for i, circuit in enumerate(circuits):
            if box in circuit:
                return i

        return -1

    def connect(self, box1: int, box2: int, circuits: list[set[int]]):
        circuit1: int = self.findCircuit(box1, circuits)
        circuit2: int = self.findCircuit(box2, circuits)
        if circuit1 < 0 and circuit2 < 0:
            s: set[int] = {box1, box2}
            circuits.append(s)
        elif circuit1 >= 0 and circuit2 >= 0 and circuit1 != circuit2:
            circuits[circuit1].update(circuits[circuit2])
            circuits.remove(circuits[circuit2])
        elif circuit1 < 0:
            circuits[circuit2].add(box1)
        else:
            circuits[circuit1].add(box2)

        return circuits

    def partTwo(self) -> None:
        total: int = 0

        sorted_map = dict(sorted(self.dist_map.items()))
        circuits: list[set[int]] = []

        for v in sorted_map.values():
            circuits = self.connect(v[0], v[1], circuits)

            if len(circuits) == 1 and len(circuits[0]) == len(self.boxes):
                total = self.boxes[v[0]][0] * self.boxes[v[1]][0]
                break

        print("Part Two - Unified X Product:", total)
