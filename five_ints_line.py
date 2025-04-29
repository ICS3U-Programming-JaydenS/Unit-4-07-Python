#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: April 29, 2025
# This program displays all the integers 1000 till 2000 5 in a row


def main():

    # Loop for the integers
    for counter in range(1000, 2000, 5):

        # Prints the integers until 1995
        if counter != 1995:
            print(
                (counter),
                (counter + 1),
                (counter + 2),
                (counter + 3),
                (counter + 4),
            )

        # When it gets to 1995 this happens
        else:
            print((counter), (counter + 1), (counter + 2), (counter + 3), (counter + 4))
            print((counter + 5))

            break
    print("Now you know all the integers up to 2000!")


if __name__ == "__main__":
    main()
