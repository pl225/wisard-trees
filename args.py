class Args:
    qtd = 0
    def __init__(self, input) -> None:
        self.input = [(e[0], e[1]) for e in input]
        self.weighted = False
        self.directed = False
        self.p = 1
        self.q = 1
        self.num_walks = 5
        self.walk_length = 10
        self.dimensions = 10
        self.window_size = 5
        self.workers = 8
        self.iter = 1
        self.OPT1 = True
        self.OPT2 = True
        self.OPT3 = False
        Args.qtd += 1
        print(Args.qtd)