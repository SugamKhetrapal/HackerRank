# Sugam Khetrapal
# take as input n denoting the number of elements in arrays X and F
n = input()
val = int(n)

# take as input n space-separated integers denoting the elements of array X
integer_list = [int(i) for i in input().split()]
# take as input n space-separated integers denoting the frequencies of array F
frequency_list = [int(i) for i in input().split()]
sum_f = sum(frequency_list)

s_list = []

for i in range(val):
    for f in range(frequency_list[i]):
        s_list.append(integer_list[i])

s_list = sorted(s_list)
index_25 = int(sum_f * 0.25)
index_50 = int(sum_f * 0.50)
index_75 = int(sum_f * 0.75)

if sum_f % 2 == 0:
    # print('Overall even number of elements')
    if (sum_f/2) % 2 == 0:
        # print('even > even')
        # print('index_25 = ', index_25)
        # print('index_75 = ', index_75)
        # print('integer_list[1] = ', s_list[1])
        # print('integer_list[index_25] = ', s_list[index_25])
        q1 = (s_list[index_25] + s_list[index_25-1]) / 2
        q2 = (s_list[index_50] + s_list[index_50-1]) / 2
        q3 = (s_list[index_75] + s_list[index_75-1]) / 2
        # q1 = s_list[index_25-1]
        # q3 = s_list[index_75-1]
    elif (sum_f/2) % 2 != 0:
        # print('even > odd')
        q1 = s_list[index_25]
        q2 = (s_list[index_50] + s_list[(index_50)-1]) / 2
        q3 = s_list[index_75]
elif sum_f % 2 != 0:
    # print('Overall odd number of elements')
    if ((sum_f-1)/2) % 2 == 0:
        # print('odd > even')
        q1 = (s_list[index_25] + s_list[index_25-1]) / 2
        q2 = s_list[index_50]
        q3 = (s_list[index_75] + s_list[index_75+1]) / 2
        # q1 = s_list[index_25-1]
        # q3 = s_list[index_75]
    elif ((sum_f-1)/2) % 2 != 0:
        # print('odd > odd')
        q1 = s_list[index_25]
        q2 = s_list[index_50]
        q3 = s_list[index_75]

# print(int(q1))
# print(int(q2))
# print(int(q3))
iqr = q3 - q1
print(float(iqr))
