from turtle import Turtle
import random
from car_3d import Car3D

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Create different car types
            car_type = random.randint(1, 4)
            random_y = random.randint(-250, 250)
            
            # Create 3D car
            new_car = Car3D(300, random_y, car_type)
            self.all_cars.append(new_car)

    def move_cars(self):
        # Move all cars and remove those that are off-screen
        cars_to_remove = []
        for car in self.all_cars:
            car.move_backward(self.car_speed)
            if car.is_off_screen():
                car.cleanup()
                cars_to_remove.append(car)
        
        # Remove off-screen cars from list
        for car in cars_to_remove:
            self.all_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
