FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsuis = fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsuis

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
    return fahrenheit

temprature = float(input('Enter the temprature: '))
temprature_type = input("Specify whether it’s in Celsius or Fahrenheit.")

if type(temprature) != 'float':
    print('You entered invalid temprature')
elif temprature_type == "Celsius":
    converter_tem = convert_to_fahrenheit(temprature)
    print(f"Your temprature converted to Fahrenheit = {converter_tem}")
elif temprature_type == "Fahrenheit":
    converter_tem = convert_to_celsius(temprature)
    print(f"Your temprature converted to Celsius = {converter_tem}")