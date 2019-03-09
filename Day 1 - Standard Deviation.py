# Sugam Khetrapal

# import necessary libraries
import statistics

# take input denoting number of elements in the array
n = input()

# take input N space-separated integers describing respective elements of the array
integer_list = [int(i) for i in input().split()]

# pstdev is for population standard deviation
# stdev is for sample standard deviation
print(round(statistics.pstdev(integer_list), 1))