# A ride object

import sys
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

        # Generate the car objects and store them in Simulation.cars. 
        # eg for i in range(1,Simulation.F+1):
        # generate car object and append to simulation.cars
        for i in range(1, self.F + 1):
            self.cars.append(Car(i))

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
                if ride.earliest_start > time_in_simulation:
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
        self.latest_start = self.f - self.distance

    # Compute the distance of this ride (manhattan distance)
    def compute_distance(self):	
        return (abs(self.a - self.x) + abs(self.b - self.y))

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
        distance_to_ride_location = (abs(self.row-ride.a) - abs(self.column - ride.b))
        time_of_arrival_at_start = self.simulation_time + distance_to_ride_location

        # Can the car get there before the ride's latest start time?
        if time_of_arrival_at_start > ride.latest_start:
            return -1 # ride is impossible 

        # If we got here, the ride is possible. Now, calculate the following:
        # How much time does the car waste DRIVING TO the start location?
        # AND
        # How much time does the car waste WAITING for the earliest_start?

        time_spent_waiting_at_start = 0
        if ride.s > time_of_arrival_at_start:
            # Take into consideration time spent waiting before the car can depart.
            time_spent_waiting_at_start = ride.s - time_of_arrival_at_start

        time_wasted = distance_to_ride_location + time_spent_waiting_at_start

        return time_wasted

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
    R, C, F, N, B, T = p.parse_simulator()
    rides = p.parse_rides()

    # create a simulation object.
    simulation = Simulation(R, C, F, N, B, T)
    i = 0
    # rides is a list of lists with information from input file
    # it is NOT a list of ride objects
    for ride in rides:
        # create Ride objects and add to simulation.unassigned_rides
        a, b, x, y, s, f = [x for x in ride]
        simulation.unassigned_rides.append(Ride(a, b, x, y, s, f, i))
        i += 1

    # TODO: COMPUTATION.
    # SOLVE THE PROBLEM.
    # ?????????????????????????????

    # Assign rides to each car. 
    for car in simulation.cars:
        can_do_more_rides = True
        while can_do_more_rides:
            # The index of the best ride in simulation.unassigned_rides
            best_ride = -1

            # The time wasted by the best ride
            least_time_wasted = sys.maxint 

            # Loop over each ride in unassigned rides
            for i in range(len(simulation.unassigned_rides)):
                # Calculate the time the car would waste if it did this ride
                time_wasted = car.time_wasted_on_ride(simulation.unassigned_rides[i])

                # If time_wasted_on_ride returned -1, the ride is NOT possible, so skip this ride.
                if time_wasted == -1:
                    continue 

                # If we get here, the ride is possible. See if it is less expensive than the current best ride.
                if time_wasted < least_time_wasted:
                    least_time_wasted = time_wasted
                    best_ride = i

            # If we DIDN'T find a ride.... best_ride is still -1. This means the driver can't take any more rides.
            if best_ride == -1:	
                can_do_more_rides = false
            else:
                print "BLAAAAAAAAAAAAAAA I HATE LIFE"
                pass
                # If we DID find a ride to do, add it to the car's ride list and udpate its internal state (position and time).
                # TODO
                # Remove the best ride from the unassigned rides list.
                # TODO
                # Add this ride to the driver's scheduled rides list.
                # TODO
                # Update the car's internal state. (Where it would be and the time the next time it has to pick a ride).
                # TODO 

    # TODO: Print our solution to file.
    simulation.write_solution_to_file()


