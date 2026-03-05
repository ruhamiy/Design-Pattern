# Target Interface
class TemperatureSensor:
    def get_temperature(self):
        pass

# Adaptee
class FahrenheitAPI:
    def get_temperature_fahrenheit(self):
        return 77 


# Adapter 
class TemperatureAdapter(TemperatureSensor):
    def __init__(self, fahrenheit_api):
        self.fahrenheit_api = fahrenheit_api

    def get_temperature(self):
        fahrenheit = self.fahrenheit_api.get_temperature_fahrenheit()

        celsius = (fahrenheit - 32) * 5 / 9

        return celsius


# Client Code
if __name__ == "__main__":
    api = FahrenheitAPI()                 # Adaptee
    adapter = TemperatureAdapter(api)     # Adapter

    temperature = adapter.get_temperature()
    print(f"Temperature in Celsius: {temperature:.2f}°C")