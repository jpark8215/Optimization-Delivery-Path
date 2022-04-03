# Jieun Park 001216539
import sys

import nearest
import package

print("All packages delivered in " + str(float("{:.2f}".format(nearest.get_overall_distance()))) + " miles")


while True:
    print("\n1) Package Lookup")
    print("2) Check Status")
    print("0) Exit Application\n")
    print()
    selected = input("Enter an option above: ")

    if selected == '0':
        sys.exit()
    if selected == '1':
        package.search_package(int(input("\nEnter package ID: ")))
    if selected == '2':
        nearest.get_status(input("Enter time in 'HH:MM:SS' format: "))
        package.search_package(int(input("\nEnter package ID: ")))







