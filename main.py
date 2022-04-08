# Jieun Park 001216539

import sys

import greedy
import hash
import package

'''
OUTPUT("All packages were delivered IN " + str(float("{:.2f}".format(greedy.get_overall_distance()))) + " miles.\n")

WHILE True:
OUTPUT("\n1> Check Status")
OUTPUT("2> Package Search")
OUTPUT("0> Exit Application\n")
OUTPUT(Notification)

SET selected TO INPUT("Please enter an option above: ")

IF selected EQUALS '0':
    sys.exit()
    
IF selected EQUALS '1':
    greedy.get_status(INPUT("Enter time IN 'HH:MM:SS' format: \n"))
    package.get_package()

    OUTPUT("\nWould you like to check the status of a package? \n2> Check status of individual package")

        IF selected EQUALS '2':
            package.search_package(int(INPUT("\nPlease enter package ID you would like to check: ")))
'''


# Gets overall distance from greedy.py and display total mileage in 2 decimal point
print("All packages were delivered in " + str(float("{:.2f}".format(greedy.get_overall_distance()))) + " miles.\n")

# O(N)
# Displays all packages including status at the specific time chosen when user selects number 1
# Displays details of selected package when user select 2 at the specific time chosen for option number 1
while True:
    print("1> Check Status of all packages")
    print("0> Exit Application\n")
    print("**Please exit application and rerun to check package status for different time**\n")

    selected = input("Please enter an option above: ")

    if selected == '0':
        sys.exit()

    if selected == '1':
        greedy.get_status(input("Enter time in 'HH:MM:SS' format: "))
        package.get_package()
        print("\nWould you like to check the status of a package? \n2> Check status of individual package")

        if selected == '2':
            package.search_package(int(input("\nPlease enter package ID you would like to check: ")))
