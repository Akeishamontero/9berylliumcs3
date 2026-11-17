class Car: #Create class Car

    def move(self): #Create method move
        print("The car drives on the road") #Print "The car drives on the road"

class Boat: #Create class Boat
   
    def move(self): #Create method move
        print("The boat sails on the water") #Print "The boat sails on the water"

class Drone: #Create class Drone

    def move(self): #Create method move
        print("The drone flies in the sky") #Print "The drone flies in the sky"

def start_trip(vehicle): #Create function start_trip with parameter vehicle
    vehicle.move() #Call the move method of the vehicle

#OBJECTS

car1 = Car()
boat1 = Boat()
drone1 = Drone()

start_trip(car1)
start_trip(boat1)
start_trip(drone1)
