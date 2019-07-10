"""
Use Cases
- User should
Classes and their relationships (statements)

ElevatorController:
- Centralized elevator system which sends a command to commands a given elevator
to move to a destination floor.
- Contains logic to move an elevator to a given floor
- Composed of a list of elevators and will also receive a command from a user

Elevator
Write some code
some ideas observer design pattern

We use a mix of observer design pattern and a command design pattern

Elevator will be the subject, ElevatorSystem will be the listener, and

Elevator notifies once in motion
"""
@dataclass
class Direction:
    UP = 'UP'
    DOWN = 'DOWN'

class ElevatorSystem:
    def __init__(self, num_elevators):
        self.elevators = []

    def call_elevator(self, current_floor: int, target_floor: int, direction: Direction):
        elevator = self.get_closest_elevator(direction)
        elevator.move(target_floor)

    def get_closest_elevator(self, current_floor: int, user_direction: Direction) -> Elevator:
        # calculate by distance to person
        min_distance = self.num_floors
        closest_el = None
        for elevator in self.elevators:
            if elevator.isMoving() or (
                elevator.getDirection() == Direction.UP and
                user_direction == Direction.UP and
                current_floor >= elevator.getFloor()
            ) or (
                elevator.getDirection() == Direction.DOWN and
                user_direction == Direction.DOWN and
                current_floor <= elevator.getFloor()
            ):
                distance = (current_floor, elevator.getFloor())

            if distance < min_distance:
                closest_el = elevator
                min_distance = distance

        return closest_el


    def calculate_distance():
        # given current floor, target floor and direction, move someone


class Elevator:
    def __init__(self, id, num_floors):
        self.main_system = ElevatorController()
        self.id = id
        self.direction = DIRECTION
        self.num_floors = num_floors

    def move(self):
        # stop at each FloatingPointError
        pass


    def notify(self):
        self.main_system.elevator_reached_destination(self.id)
