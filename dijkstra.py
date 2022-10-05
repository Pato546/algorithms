# Restructure the algorithm


class NotSolvedException(Exception):
    pass


class DijkstraAlgorithm:
    def __init__(self, graph: dict, start: str):
        self.graph = graph
        self.start = start
        self.processed: set = set()
        self.costs = self._costs()
        self.parents = self._parents()
        self.solved = False

    # @property
    # def parents(self):
    #     pass

    def _costs(self) -> dict:
        # this is the cost of the neighbors of the start node
        neighbors_start = self.graph[self.start]

        for key in self.graph.keys():
            if key in neighbors_start or key == self.start:
                continue
            neighbors_start[key] = float("inf")

        return neighbors_start

    def _parents(self) -> dict:
        parents = {}  # this stores the initial parents of the nodes
        for key in self.costs.keys():
            if self.costs[key] != float("inf"):
                parents[key] = self.start
            else:
                parents[key] = None

        return parents

    def find_lowest_node(self):
        lowest_node = None
        lowest_cost = float("inf")
        for key, val in self.costs.items():
            if key not in self.processed and val < lowest_cost:
                lowest_cost = val
                lowest_node = key

        return lowest_node

    def solve(self):

        node = self.find_lowest_node()

        while node is not None:
            cost: int = self.costs[node]  # get the cost of the node
            neighbors: dict = graph[node]

            for key, val in neighbors.items():
                new_cost = cost + val
                if new_cost < self.costs[key]:
                    self.costs[key] = new_cost
                    self.parents[key] = node
            self.processed.add(node)
            node = self.find_lowest_node()

        return self.costs


if __name__ == "__main__":
    graph: dict = {
        "1": {"2": 10, "3": 50},
        "2": {"4": 30, "5": 70},
        "3": {"4": 10, "5": 60},
        "4": {"5": 30, "6": 60},
        "5": {"6": 30},
        "6": {},
    }

    dijkstra_algorithm = DijkstraAlgorithm(graph=graph, start="1")
    print(dijkstra_algorithm.solve())
    print(dijkstra_algorithm.parents)
