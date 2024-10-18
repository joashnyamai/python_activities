#Python classes and objects in Temperature
class Temperature:
    def convertFahrenheit(self, celsius):
        """Converts Celsius to Fahrenheit and prints the result."""
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    def convertCelsius(self, fahrenheit):
        """Converts Fahrenheit to Celsius and prints the result."""
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")

temp = Temperature()


celsius_input = float(input("Enter temperature in Celsius: "))
temp.convertFahrenheit(celsius_input)


fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
temp.convertCelsius(fahrenheit_input)
