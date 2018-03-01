# A ride object

from sys import argv

from parser import Parser


class Simulation:
    def __init__(self, R, C, F, N, B, T):
        self.R = R # number of rows on the grid
        self.C = C # number of columns on the grid
        self.F = F # number of vehicles in the fleet
        self.N = N # number of rides
        self.B = B # per-ride bonus for starting the ride on time
        self.T = T # total amount of steps in the simulation
        self.cars = []
        self.unassigned_rides = []

        # TODO: write the solution to file.
        # Do this by looping over each car in cars.
        # car_ID_1 ride_id_0 ride_id_1 ... ride_id_n
        # ...
        # car_ID_F ride_id_0 ... ride_id_n

    def write_solution_to_file(self):
        print("TODO: implement write solution to file method of Simulation object")
        pass

    def compute_points(self):
        total_points = 0
        for car in self.cars:
            time_in_simulation = 0
            for ride in car.rides:
                if ride.earliest_start > time_in_simulation
                    total_points += ride.distance + self.B
                else:
                    total_points += ride.distance

                time_in_simulation += ride.distance


class Ride:
        def __init__(self, row_of_start, column_of_start, row_of_finish, column_of_finish, earliest_start, latest_finish, ID):
            self.ID = ID # the ID of the ride, from 0 to N-1
            self.a = row_of_start
            self.b = column_of_start
            self.x = row_of_finish
            self.y = column_of_finish
            self.s = earliest_start
            self.f = latest_finish
            self.distance = self.compute_distance()
            self.latest_start = self.latest_finish - self.distance

        # Compute the distance of this ride (manhattan distance)
        def compute_distance(self):	
            return (abs(this.a - this.x) + abs(this.b - this.y))

class Car:
	def __init__(self, ID):
            self.ID = ID # the index of this car. From 1 to Simulation.F.
            self.rides = [] # The simulation should populate this list with the rides that a car will take.
            self.column = 0
            self.row = 0
            self.simulation_time = 0

	def time_wasted_on_ride(self, ride):
            pass

        def reset(self):
            column = 0
            row = 0
            simulatin_time = 0



if __name__ == "__main__":
    print(" ")
    print("----------------------------")
    print("Hashcode 2018 TEAM BING WHOO")
    print("----------------------------")
    print(" ")

    script, filename = argv
    p = Parser(filename)

    # TODO: Open the file. Assign variables R, C, F, N, B, T.

    R, C, F, N, B, T = p.parse_simulator()
    print "Rows: %d" % R
    print "Columns: %d" % C
    print "Vehicles: %d" % F
    print "Rides: %d" % N
    print "Bonus: %d" % B
    print "Time: %d" % T
    print ""

    rides = p.parse_rides()

    for ride in rides:
        # create Ride objects and add to simulation.unassigned_rides
        print ride

    # TODO: create a simulation object.
    simulation = Simulation(R, C, F, N, B, T)

    # TODO: Generate the car objects and store them in Simulation.cars. 
    # eg for i in range(1,Simulation.F+1):
    # generate car object and append to simulation.cars

    # TODO: COMPUTATION.
    # SOLVE THE PROBLEM.
    # ?????????????????????????????

    # TODO: Print our solution to file.
    simulation.write_solution_to_file()

