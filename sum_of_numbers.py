# Created by: Ferdous Sediqi
# Created on: April. 17 2022
# created by: Ferdous Sediqi
# Modified on: April 19, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number also display invalid input

def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_num_as_string = input("Enter a positive number: ")
    print("")

    try:
        user_num_as_int = int(user_num_as_string)
        # calculate the sum of all numbers from 0 to user number
        while (loop_counter <= user_num_as_int):
            sum = sum + loop_counter
            print("Tracking {} times through loop.".format(loop_counter))
            print("")
            loop_counter = loop_counter + 1
            # print("The sum of the numbers from 0 to {} is:
            # {}.".format(user_num_as_int, sum))
            if user_num_as_int < 0:
                print("Input was not a positive number.")
    except Exception:
        print("")
        print("input is not a integer.")


if __name__ == "__main__":
    main()
