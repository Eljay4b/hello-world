from random import randint
class Vehicle:
    id = 0
    passengers = 0
    def __init__(self,min,max):
        self.passengers = randint(min,max)
        Vehicle.id += 1
        #self.id = Vehicle.id
        Vehicle.passengers += self.passengers
    def __str__(self):
        return f" ::  Number of Passengers : {self.passengers}" #Vehicle #: {Vehicle.id} #vehicles version
        return f"[Vehicle {Vehicle.id}] Number of Passengers : {self.passengers}" # peder version

class Bus(Vehicle):
    id=0
    def __init__(self):
        Bus.id +=1
        #self.id = Bus.id
        super().__init__(5,20)
        Bus.passengers += self.passengers

class Car(Vehicle):
    id=0
    def __init__(self):
        Car.id +=1
        #self.id = Car.id
        super().__init__(1,4)
        Car.passengers += self.passengers

def main():
    cars = []
    busses=[]
    # lets create cars and busses
    for i in range(1,6):
        cars.append(Car())
        busses.append(Bus())
    print("-"*40)
    print(f"Bus Passengers: {Bus.passengers}" )
    print(f"Car Passengers: {Car.passengers}" )
    VehiclePassengers = Bus.passengers + Car.passengers
    print(f"Vehicle Passengers: {VehiclePassengers}")
    print("-"*40)

    for bus in busses:
        print(f"Bus # {bus.id} {bus}")
    for car in cars:
        print(f"Car # {car.id} {car}")

if __name__ == "__main__":
    main()
