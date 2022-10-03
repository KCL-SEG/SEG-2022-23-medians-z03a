"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        if (len(numbers)%2)== 0:
            median = (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2)-1])/2
        else:
            median = numbers[int(len(numbers)/2)]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        print (median)
        break


