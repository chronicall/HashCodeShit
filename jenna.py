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

		# ---STATE VARIABLES ----
		self.row = 0
		self.column = 0
		self.simulation_time = 0
		# ----------

	# Return -1 if the ride is impossible.
	# Otherwise, return the amount of time the car spends combined travelling to the ride AND waiting for ride to start.
	def time_wasted_on_ride(self, ride):
		# 1. Check whether ride is possible.

		# A ride is possible if (1) the driver can get there before ride.latest_start 
		#
		distance_to_ride_location = (abs(self.row-ride.row_of_start) - abs(self.column- ride.colum_of_start))
		time_of_arrival_at_start = self.simulation_time + distance_to_ride_location

		# Can the car get there before the ride's latest start time?
		if time_of_arrival_at_start > ride.latest_start:
			return -1 # ride is impossible 

		# If we got here, the ride is possible. Now, calculate the following:
		# How much time does the car waste DRIVING TO the start location?
		# AND
		# How much time does the car waste WAITING for the earliest_start?


		if ride.earliest_start > time_of_arrival_at_start:
			# Take into consideration time spent waiting before the car can depart.
			time_spent_waiting_at_start = ride.earliest_start - time_of_arrival_at_start

		time_wasted = distance_to_ride_location + time_spent_waiting_at_start

		return time_wasted
		
		
		

		pass

	def update(self, t, column, row):
		self.simulation_time = self.simulation_time + t
		self.column = column
		self.row = row





if __name__ == "__main__":
    print(" ")
    print("----------------------------")
    print("Hashcode 2018 TEAM BING WHOO")
    print("----------------------------")
    print(" ")

    script, filename = argv
    p = Parser(filename)

    # TODO: Open the file. Assign variables R, C, F, N, B, T.

    R, C, F, N, B, T = p.parseSimulator()
    print "Rows: %d" % R
    print "Columns: %d" % C
    print "Vehicles: %d" % F
    print "Rides: %d" % N
    print "Bonus: %d" % B
    print "Time: %d" % T
    print ""

    rides = p.parseRides()

    for ride in rides:
        print ride

    # TODO DELET
   

    # TODO: create a simulation object.
    simulation = Simulation(R, C, F, N, B, T)

    d = simulation



    # TODO: Generate the car objects and store them in Simulation.cars. 
    # eg for i in range(1,Simulation.F+1):
    # generate car object and append to simulation.cars

    # TODO: COMPUTATION.
    # SOLVE THE PROBLEM.
    # ?????????????????????????????

    # TODO: Print our solution to file.
    simulation.write_solution_to_file()


