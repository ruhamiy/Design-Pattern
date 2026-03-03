from abc import ABC, abstractmethod

# Product Interface
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self):
        print("Deliver by land ")

class Ship(Transport):
    def deliver(self):
        print("Deliver by sea ")

# Creator
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

# Client
if __name__ == "__main__":
    road = RoadLogistics()
    road.plan_delivery()

    sea = SeaLogistics()
    sea.plan_delivery()