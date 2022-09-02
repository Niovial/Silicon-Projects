from decimal import Clamped


def menu():
    print("Select the operation you would like to perform:")
    option = int(input("""
            1: Traversing
            2: Inserting
            3: Deleting        
        """))
    return option


def create_array():
    # Initialize array
    array = []
    array_size = int(input("Enter your array size (a number):"))
    print("Enter the elements of your array:")
    for i in range(array_size):
        element = input()
        if element == "":
            # Although None is not 0, for the purposes of this assignment
            # take it that None is 0.
            element = None
            # Append basically means increase the array size by one
            # and then add an element to that location
            # None is not the same as "".
        array.append(element)

    return array


def traversing(array):
    print("The elements of your traversed array are:")
    for i in array:
        print(i)


def inserting(array):
    array_size = len(array)
    print("Where in your array would you like to insert an element:")
    option = int(input("""
        1: Middle
        2: End
    """))
    inserted_element = input("Enter the element you would like to insert:")

    if option == 1:
        # Find the index of the array's midpoint and make it an integer.
        midpoint_index = array_size / 2
        # No array index can be anything other than a whole number (integer)
        if (midpoint_index % 2) != 0:
            # if array_size / 2 gives a mixed number or fraction, 
            # add 0.5 to make it a whole number
            midpoint_index += 0.5

        # Then convert whole number into an integer. If midpoint_index was 1.5 
        # adding 0.5 to it will make 2.0. The code below will change it to 2.
        # 2.0 is a fraction, 2 is an integer
        midpoint_index = int(midpoint_index)

        # Increase the array size by one
        # Insert the element at the last array index
        array_size += 1
        array.append(inserted_element)

        # Loop starts from last array index and stops at midpoint
        # -1 is the step of loop so the loop moves backwards 
        # similar to writing i-- instead of i++ in C++
        for i in range(array_size - 1, midpoint_index, -1):
            # Store the element you want to shift from its location
            shifted_element = array[i]
            # Assign the next element to last element's location
            array[i] = array[i - 1]

            # Assign the last element to the next element's location.
            # if [2, 4, 6] is my array, array size is 3, size will 
            # increase by one and midpoint index will become 2 (1.5+0.5)
            # see comments on midpoint index
            array[i - 1] = shifted_element

    elif option == 2:
        array_size += 1
        array.append(inserted_element)

    print(array)


def deleting(array):
    print(f"Your array is {array}.")
    # The code below is a very simple way of removing an element from an array.
    # But in accordance with the question, you want to work with element locations.
    # However, for simplicity's sake, this code will be used.
    element = input("Enter the element you would like to delete from your array:")
    array.remove(element)

    print(f"The deleted element was {element}.")
    print(f"Your new array is {array}.")



def program():
    choice = menu()
    array = create_array()
    if choice == 1:
        traversing(array)
    elif choice == 2:
        inserting(array)
    elif choice == 3:
        deleting(array)


program()