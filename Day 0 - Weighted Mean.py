# Sugam Khetrapal

# take integer input
n = input()

# take list of integers as input
integer_list = [int(i) for i in input().split()]

# take list of weights as input
weights_list = [int(i) for i in input().split()]

# if numpy were allowed
# print(numpy.average(integer_list, weights = weights_list))

s = 0
for i, w in zip(integer_list, weights_list):
    s += i * w

average = s / sum(weights_list)
print(round(average, 1))
