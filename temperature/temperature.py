""" convert the temperature between degress fahrenheit and degress celsius"""
def to_celsius(fahrenheit):
    """ Accept Fahrenheit """
    celsius = (fahrenheit -32) * 5/9
    return celsius


def to_fahrenheit(celsius):
    """ Accept celsius """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit