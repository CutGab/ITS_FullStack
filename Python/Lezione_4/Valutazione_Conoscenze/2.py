# Scrivi una funzione che converte una temperatura da gradi Celsius a Fahrenheit e viceversa a seconda del parametro to_fahrenheit. Utilizza il concetto di parametri opzionali per il parametro to_fahrenheit.

# For example:

# Test
# print(convert_temperature(0))
# Result
# 32.0

# print(convert_temperature(32, False))
# Result
# 0.0

def convert_temperature(temp: float, to_farenheit = True):

    if to_farenheit == False:

        return (temp - 32) * 5/9

    else:

        return (temp * 5/9) + 32

print(convert_temperature(32, to_farenheit = False))
print(convert_temperature(0))