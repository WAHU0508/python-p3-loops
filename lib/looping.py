#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squared = [square * square for square in int_list]
    return squared

def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if (i % 3 == 0):
            if (i % 5 == 0):
                print("FizzBuzz")
            else:
                print("Fizz")
        elif (i % 5 == 0):
            if (i % 3 == 0):
                print("FizzBuzz")
            else:
                print("Buzz")
        else:
            print(f"{i}")
        i += 1
