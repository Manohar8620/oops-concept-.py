class car:
    def __init__(self,colour,max_speed,accelaration,tyre_friction):
        self.colour = colour
        self.max_speed = max_speed
        self.acceleration = accelaration
        self.tyre_friction = tyre_friction
        self.current_speed = 0


    def start_engine(self):
        self.is_engine_started = True

    def start_engine(self):
        self.is_engine_stop = False

    def acceleration(self):
        if not self.is_engine_started :
            print("car is not started at")
        else:
            self.current_speed = current_speed + self.acceleration
            if current_speed > self.max_speed:
                self.current_speed = self.max_speed


def default_test():
    car=car(colour='red',max_speed=250,acceleration=10,tyre_friction=3)
    print(car.is_engine_started)
    car.start_engine()
    print(car.is_engine_started)
    car.start_engine()
    print(car.is_engine_started)
    car.start_engine()

    car.acceleration()
    print(car.current_speed)
    car.start_engine()
    print(car.current_speed)
    car.acceleration()
    print(car.curent_speed)
    car.acceleration()
    car.acceleration()
