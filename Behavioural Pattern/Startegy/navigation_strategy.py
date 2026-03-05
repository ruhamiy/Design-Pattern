from abc import ABC, abstractmethod

# STRATEGY INTERFACE

class RouteStrategy(ABC):

    @abstractmethod
    def build_route(self, start, destination):
        pass

# CONCRETE STRATEGIES

class CarRouteStrategy(RouteStrategy):

    def build_route(self, start, destination):
        return f" Driving route from {start} to {destination} via highways and main roads."


class WalkingRouteStrategy(RouteStrategy):

    def build_route(self, start, destination):
        return f" Walking route from {start} to {destination} via pedestrian paths and shortcuts."


class CyclingRouteStrategy(RouteStrategy):

    def build_route(self, start, destination):
        return f" Cycling route from {start} to {destination} via bike-friendly roads."


# CONTEXT 

class Navigator:

    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def build_route(self, start, destination):
        return self._strategy.build_route(start, destination)


# CLIENT CODE

if __name__ == "__main__":

    navigator = Navigator(CarRouteStrategy())

    print(navigator.build_route("Addis Ababa", "Bole"))

    print("\nSwitching strategy...\n")

    navigator.set_strategy(WalkingRouteStrategy())
    print(navigator.build_route("Addis Ababa", "Bole"))

    print("\nSwitching strategy again...\n")

    navigator.set_strategy(CyclingRouteStrategy())
    print(navigator.build_route("Addis Ababa", "Bole"))