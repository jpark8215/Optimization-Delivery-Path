# Jieun Park 001216539
import sys

import nearest
import package

# Gets overall distance from nearest.py and display total mileage in 2 decimal point
print("All packages delivered in " + str(float("{:.2f}".format(nearest.get_overall_distance()))) + " miles\n")

# O(N)
# Displays all packages including status at the specific time chosen when user selects number 1
# Displays details of selected package when user select 2 at the specific time chosen for option number 1
while True:
    print("1> Check Status")
    print("2> Package Search")
    print("0> Exit Application\n")
    print()
    selected = input("Please enter an option above: ")

    if selected == '0':
        sys.exit()
    if selected == '1':
        nearest.get_status(input("Enter time in 'HH:MM:SS' format: "))
        print(package.get_package())
    if selected == '2':
        # while True:
        # print("1: Search by ID")
        # print("2: Search by Address\n")
        # print()
        # selected = input("Please enter an option above: ")
        #
        # if selected == '1':
        # nearest.get_status(input("Enter time in 'HH:MM:SS' format: "))
        package.search_package(int(input("\nEnter package ID: ")))

        # if selected == '2':
        #     package.search_package_address(str(input("\nEnter package Address: ")))
