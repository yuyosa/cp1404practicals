from unreliable_car import UnreliableCar
my_car = UnreliableCar("car1", 100, 75 )
print("Initial state:", my_car)

distance_driven = my_car.drive(40)
print("Distance driven:", distance_driven)
print("Final state:", my_car)