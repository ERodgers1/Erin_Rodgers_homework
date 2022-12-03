def C_to_F(celsius):
    if celsius < -273.15:
        raise ValueError('The temperature is below absolute zero.')
    else:
        fahrenheit = ((9/5) * celsius) + 32
        return fahrenheit

def F_to_C(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError('The temperature is below absolute zero.')
    else:
      celsius = (fahrenheit - 32) * (5/9)
      return celsius
