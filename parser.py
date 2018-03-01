class Parser:
    def __init__(self, filename):
        self.inp = open(filename)

    def parse_simulator(self):
        R, C, F, N, B, T = [int(x) for x in self.inp.readline().split()]

        return R, C, F, N, B, T

    def parse_rides(self):
        rides = []
        for line in self.inp:
            a, b, x, y, s, f = [int(x) for x in line.split()]
            rides.append([a, b, x, y, s, f])

        return rides

