"""
Head First Design Patterns
Ch 1
"""
import abc
# Behaviors to fly
class FlyBehavior(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class AircraftFlyingBehavior(FlyBehavior):
    def fly(self):
        print("Flying an aeroplane!")

class BirdFlyingBehavior(FlyBehavior):
    def fly(self):
        print("Flying with my own wings!")

class ParrotFlyingBehavior(FlyBehavior):
    def fly(self):
        print("Im a parrot and do not fly actually")

# A duck is composed of a behavior to quack but can be changed
# dynamically at runtime to support differnt behaviors
class Duck:
    # Thru the magic of polymorphism, can dynamically assign
    # a different quack behavior implementation at runtime
    def __init__(self, fly_behavior: FlyBehavior):
        self.flyer = fly_behavior

    def fly(self):
        self.flyer.fly()

    # Allows user to set behavior dynamically at runtime
    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.flyer = fly_behavior

# Inheritance isn't always best, what if it's
class Plane(AircraftFlyingBehavior):
    def fly(self):
        super().fly()

d = Duck(fly_behavior=BirdFlyingBehavior())
d.fly()
d.set_fly_behavior(ParrotFlyingBehavior())
d.fly()
p = Plane()
p.fly()
