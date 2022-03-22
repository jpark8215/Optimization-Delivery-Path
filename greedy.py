# # Greedy Algorithm - START
# # Greedy Algorithm: Min Expenses => Max Profits
# import math
# def greedyAlgorithmMinExpenses(budget):
#     total = budget
#     c25dollar = 0
#     c10dollar = 0
#     c5dollar = 0
#     c1dollar = 0
#     while (budget >= 25):
#         if c25dollar > 3: # why 3? 0,1,2,3 will not break so 4 times.
#             break
#         c25dollar += 1
#         budget = budget - 25
#     while (budget >= 10):
#         c10dollar += 1
#         budget = budget - 10
#     while (budget >= 5):
#         c5dollar += 1
#         budget = budget - 5
#     while (budget > 0):
#         if c1dollar > 3:
#             break
#         c1dollar += 1
#         budget = budget - 1
#
#     cDVDs = c25dollar + c10dollar + c5dollar + c1dollar
#
#     # expense calculation
#     eDVDs = 1.00 * cDVDs # Material cost of DVD: $1.00
#     eLabor = 12.00 * (math.ceil(cDVDs/10)) # Labor is $12.00 for every 10 DVDs, $24.00 for 11 DVDs
#     eShipping = 0.50 * cDVDs # Shipping cost is $0.50 per DVD
#     eTotal = eDVDs + eLabor + eShipping
#     profit = total - eTotal
#
#     print("${:.2f}-Budget, {}-DVDs, ${:.2f}-Expense, ${:.2f}-Profit ==>".format(total,cDVDs,eTotal,profit))
#     print(" {} x 25 dollar movie = ${:.2f}".format(c25dollar,c25dollar*25.00))
#     print(" {} x 10 dollar movie = ${:.2f}".format(c10dollar,c10dollar*10.00))
#     print(" {} x 5  dollar movie = ${:.2f}".format(c5dollar,c5dollar*5.00))
#     print(" {} x 1  dollar movie = ${:.2f}".format(c1dollar,c1dollar*1.00))
# # ---------------------------------------------------------
#
#
# print("\nGreedy Algorithm: Min Expenses => Max Profits")
# greedyAlgorithmMinExpenses(102) # $102.00 budget
# greedyAlgorithmMinExpenses(94) # $94.00 budget
# greedyAlgorithmMinExpenses(71) # $71.00 budget
# greedyAlgorithmMinExpenses(200) # $200.00 budget
# This file takes data from the distance csv file, creates vertices based on the name of the location,
# and graphs the data using undirected edges. Each edge has a weight that represents the miles between each vertex


