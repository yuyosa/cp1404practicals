from car import Car
import random
class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance = random.random() * 100
        if chance < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven

    def __str__(self):
        return f"{super().__str__()},reliability is {self.reliability}"