# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# base class for all Vehicles


class Vehicle:
    pass

# base for Car and Motorcycle


class GroundVehicle(Vehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass

# base for all Flying Vehicles aka Airplane & Starship


class FlightVehicle(Vehicle):
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
