# Jieun Park 001216539
import sys

import greedy
import package

'''
OUTPUT("All packages were delivered IN " + str(float("{:.2f}".format(greedy.get_overall_distance()))) + " miles.\n")

WHILE True:
    OUTPUT("1> Check Status")
    OUTPUT("0> Exit Application\n")
    OUTPUT()

    SET selected TO INPUT("Please enter an option above: ")

    IF selected EQUALS '0':
        sys.exit()

    IF selected EQUALS '1':
        greedy.get_status(INPUT("Enter time IN 'HH:MM:SS' format: "))
        OUTPUT(package.get_package())
        package.search_package(int(INPUT("\nEnter package ID you would like to check: ")))
'''

# Gets overall distance from greedy.py and display total mileage in 2 decimal point
print("All packages were delivered in " + str(float("{:.2f}".format(greedy.get_overall_distance()))) + " miles.\n")

# O(N)
# Displays all packages including status at the specific time chosen when user selects number 1
# Displays details of selected package when user select 2 at the specific time chosen for option number 1
while True:
    print("1> Check Status")
    # print("2> Package Search")
    print("0> Exit Application\n")
    print()
    selected = input("Please enter an option above: ")

    if selected == '0':
        sys.exit()
    if selected == '1':
        greedy.get_status(input("Enter time in 'HH:MM:SS' format: "))
        print(package.get_package())
        package.search_package(int(input("\nEnter package ID you would like to check: ")))
