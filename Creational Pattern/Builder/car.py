from abc import ABC, abstractmethod

# PRODUCT 1 — CAR


class Car:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return (
            f"Car:\n"
            f"- Seats: {self.seats}\n"
            f"- Engine: {self.engine}\n"
            f"- Trip Computer: {self.trip_computer}\n"
            f"- GPS: {self.gps}\n"
        )


# PRODUCT 2 — MANUAL


class Manual:
    def __init__(self):
        self.content = []

    def add(self, text):
        self.content.append(text)

    def __str__(self):
        return "Car Manual:\n" + "\n".join(self.content)


# BUILDER INTERFACE


class Builder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seats(self, seats):
        pass

    @abstractmethod
    def set_engine(self, engine):
        pass

    @abstractmethod
    def set_trip_computer(self, value):
        pass

    @abstractmethod
    def set_gps(self, value):
        pass


# CONCRETE BUILDER — CAR BUILDER

class CarBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()

    def set_seats(self, seats):
        self.car.seats = seats

    def set_engine(self, engine):
        self.car.engine = engine

    def set_trip_computer(self, value):
        self.car.trip_computer = value

    def set_gps(self, value):
        self.car.gps = value

    def get_product(self):
        product = self.car
        self.reset()
        return product


# CONCRETE BUILDER — MANUAL BUILDER

class CarManualBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self.manual = Manual()

    def set_seats(self, seats):
        self.manual.add(f"Car has {seats} seats.")

    def set_engine(self, engine):
        self.manual.add(f"Engine type: {engine}")

    def set_trip_computer(self, value):
        if value:
            self.manual.add("Trip computer included.")
        else:
            self.manual.add("No trip computer.")

    def set_gps(self, value):
        if value:
            self.manual.add("GPS included.")
        else:
            self.manual.add("No GPS.")

    def get_product(self):
        product = self.manual
        self.reset()
        return product


# DIRECTOR

class Director:

    def construct_sports_car(self, builder: Builder):
        builder.reset()
        builder.set_seats(2)
        builder.set_engine("Sport Engine V8")
        builder.set_trip_computer(True)
        builder.set_gps(True)

    def construct_suv(self, builder: Builder):
        builder.reset()
        builder.set_seats(5)
        builder.set_engine("SUV Engine")
        builder.set_trip_computer(True)
        builder.set_gps(True)


# CLIENT CODE

if __name__ == "__main__":

    director = Director()

    # Build Car
    car_builder = CarBuilder()
    director.construct_sports_car(car_builder)
    car = car_builder.get_product()

    print("===== CAR =====")
    print(car)

    # Build Manual
    manual_builder = CarManualBuilder()
    director.construct_sports_car(manual_builder)
    manual = manual_builder.get_product()

    print("===== MANUAL =====")
    print(manual)