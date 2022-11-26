class Args:
    def __init__(self, input) -> None:
        self.input = [(e[0], e[1]) for e in input]
        self.weighted = False
        self.directed = False
        self.p = 1
        self.q = 1
        self.num_walks = 10
        self.walk_length = 30
        self.dimensions = 20
        self.window_size = 10
        self.workers = 8
        self.iter = 1