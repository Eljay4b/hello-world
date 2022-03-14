'''
Write a program detailing the number of passengers per vehicle.
The program includes three classes:
Vehicle, Car, Bus where Vehicle is the parent class of Car and Bus.

a) [10 pts] Each of the Car and Bus classes should have a constructor method __init()__
 that generates and returns a random number of passengers based on the type of the vehicle;
If it is a Bus, then the number of passengers should be within a range of 5 and 20.
If the vehicle is a Car, the range should be between 1 to 4 passengers, inclusively.

b) [10 pts] The program's main() function would display the following output.
Notably, since the numbers of passengers are randomly selected,
the program will keep changing them every time it runs.

--------------------------------
Bus Passengers:   64
Car Passengers:   13
Total Passengers: 77
--------------------------------
Bus#:  1  Number of Passengers :18
Bus#:  2  Number of Passengers :20
Bus#:  3  Number of Passengers : 6
Bus#:  4  Number of Passengers : 9
Bus#:  5  Number of Passengers :11
Car#:  6  Number of Passengers : 1
Car#:  7  Number of Passengers : 2
Car#:  8  Number of Passengers : 4
Car#:  9  Number of Passengers : 2
Car#: 10  Number of Passengers : 4
--------------------------------
c) [5 pts] Restructure the program by re-defining the Bus class to be the superclass of Car, and display the same output.

'''
from random import randint

class Vehicle:
    id = 0
    passengers = 0
    def __init__(self,min,max):
        self.passengers = randint(min,max)
        Vehicle.id +=1
    def __repr__(self):
        return f"[Vehicle {Vehicle.id}] Number of Passengers : {self.passengers}"

class Bus(Vehicle):
    id=0
    def __init__(self):
        Bus.id +=1
        super().__init__(5,20)

class Car(Vehicle):
    id=0
    def __init__(self):
        Car.id +=1
        super().__init__(1,4)



def main():
    print("-"*40)
    # bus1 = Bus()
    # print(bus1)
    # car1 = Car()
    # print(car1)

    fleet=[]
    for i in range(1,6):
        b = Bus()
        print("Bus# ",Bus.id,": ",b)
    for i in range(1,6):
        c = Car()
        print("Car# ",Car.id,": ",c)

#This can by even more "DRY"
if __name__ == "__main__":
    main()
