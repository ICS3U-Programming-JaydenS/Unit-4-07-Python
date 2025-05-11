#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: April 29, 2025
# This program displays all the integers 1000 till 2000 5 in a row


def main():

    # Loop for the integers
    for counter in range(1000, 2001, 1):

        # Checks for all cases of the remainder
        if counter % 5 == 0:
            print(counter, end=" ")
        elif counter % 5 == 1:
            print((counter), end=" ")
        elif counter % 5 == 2:
            print((counter), end=" ")
        elif counter % 5 == 3:
            print((counter), end=" ")
        elif counter % 5 == 4:
            print(counter)


if __name__ == "__main__":
    main()
