"""
def fizzbuzz(number):

    if number % 15 == 0:
        return 'fizzbuzz'
    
    if number % 3 == 0:
        return 'fizz'

    if number % 5 == 0:
        return 'buzz'
    
    return str(number)
"""

def fizzbuzz(number):
    ret = ""
    if number % 3 == 0:
        ret += "fizz"
    if number % 5 == 0:
        ret += "buzz"
    return ret or str(number)
