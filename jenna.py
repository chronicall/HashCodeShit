# A ride object

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

	# Compute the distance of this ride (manhattan distance)
	def compute_distance(self):	
		return (abs(this.a - this.x) + abs(this.b - this.y))

class Car:
	def __init__(self, ID):
		self.ID = ID # the index of this car. From 1 to Simulation.F.
		self.rides = [] # The simulation should populate this list with the rides that a car will take. 


if __name__ == "__main__":

	print("----------------------------")
	print("Hashcode 2018 TEAM BING WHOO")
	print("----------------------------")

	# TODO: Open the file. Assign variables R, C, F, N, B, T.

	R = 0
	C = 0
	F = 0
	N = 0
	B = 0
	T = 0

	# TODO: create a simulation object.
	simulation = Simulation(R, C, F, N, B, T)
	

	# TODO: Generate the car objects and store them in Simulation.cars. 
	# eg for i in range(1,Simulation.F+1):
		# 


	# TODO: Generate the ride objects and store them in Simulation.rides.
	