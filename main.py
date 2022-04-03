# Jieun Park 001216539
import sys

import nearest
import package

print("All packages delivered in " + str(float("{:.2f}".format(nearest.get_overall_distance()))) + " miles\n")


while True:
    print("1: Check Status")
    print("2: Package Search")
    print("0: Exit Application\n")
    print()
    selected = input("Please enter an option above: ")

    if selected == '0':
        sys.exit()
    if selected == '1':
        nearest.get_status(input("Enter time in 'HH:MM:SS' format: "))
    if selected == '2':
        package.search_package(int(input("\nEnter package ID: ")))







