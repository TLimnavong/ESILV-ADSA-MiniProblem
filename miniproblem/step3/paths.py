# step3/paths.py

from ..graph.shortest_path import FloydWarshall


class Proofs():
    def __init__(self):
        pass

    @staticmethod
    def run():
        crewmatesMap = [
            [0, 5, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 5, 4, 4, 0, 6, 0, 0, 0, 0, 0, 0, 0],
            [5, 5, 0, 4, 0, 5, 0, 8, 0, 0, 0, 0, 0, 0],
            [3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 4, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
            [0, 6, 0, 0, 3, 0, 0, 3, 3, 1, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 4, 3, 0, 2, 0, 0, 0, 4, 4],
            [0, 0, 0, 0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 2, 7, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 4, 6, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 7, 6, 8, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 2, 0]
        ] # Adjacency matrix representing the crewmates' map as a graph
        impostorsMap = [
            [0, 3, 6, 8, 0, 0, 0],
            [3, 0, 3, 4, 0, 0, 0],
            [6, 3, 0, 3, 0, 1, 5],
            [8, 4, 3, 0, 4, 4, 0],
            [0, 0, 0, 4, 0, 2, 0],
            [0, 0, 1, 4, 2, 0, 2],
            [0, 0, 0, 0, 0, 2, 0]
        ] # Adjacency matrix to represent imposotors' map as a graph
        FloydWarshall.run(crewmatesMap, "assets/crewmates.txt")
        FloydWarshall.run(impostorsMap, "assets/impostors.txt")
        print("Matrices saved in assets as txt files \n\n")
