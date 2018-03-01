class Parser:
    def __init__(self, filename):
        self.inp = open(filename)

    def parseSimulator(self):
        R, C, F, N, B, T = [int(x) for x in self.inp.readline().split()]

        return R, C, F, N, B, T
        """
            print "R: %d" % R
            print "C: %d" % C
            print "F: %d" % F
            print "N: %d" % N
            print "B: %d" % B
            print "T: %d" % T
            print ""
        """

    def parseRides(self):
        rides = []
        for line in self.inp:
            a, b, x, y, s, f = [int(x) for x in line.split()]
            rides.append([a, b, x, y, s, f])

        return rides
        """
            print "a: %d" % a
            print "b: %d" % b
            print "x: %d" % x
            print "y: %d" % y
            print "s: %d" % s
            print "f: %d" % f
            print ""
        """

