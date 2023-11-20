#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end=" ")
            count += 1
    except IndexError:
        pass  # Stop the loop if IndexError occurs (x is greater than the length of my_list)

    print()  # New line after printing elements
    return count
