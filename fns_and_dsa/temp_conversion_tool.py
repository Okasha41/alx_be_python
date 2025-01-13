FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(f):
    c = (f - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return c

def convert_to_fahrenheit(c):
    f = (c * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return f

temprature = float(input('Enter the temperature to convert:'))
temprature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type(temprature) != 'float':
    print('You entered invalid temprature')
elif temprature_type != "F" and temprature_type != "C":
    print('You entered invalid temprature type')
elif temprature_type == "C":
    converter_tem = convert_to_fahrenheit(temprature)
    print(f"{temprature}°C is {converter_tem}°F")
elif temprature_type == "F":
    converter_tem = convert_to_celsius(temprature)
    print(f"{temprature}°F is {converter_tem}°C")