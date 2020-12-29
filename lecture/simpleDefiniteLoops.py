# for i in [5, 4, 3, 2, 1] :
#     print(i)
# print('Blastoff')

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print('Happy New Year:', friend)
# print('Done!')

# largest_so_far = -1
# print('Before', largest_so_far)
# for the_num in [9, 41, 12, 3, 74, 15] :
#     if the_num > largest_so_far :
#         largest_so_far = the_num
#     print(largest_so_far, the_num)
# 
# print('After', largest_so_far)

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
#    if smallest is None:
#        smallest = itervar
#    elif itervar < smallest:
#        smallest = itervar
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)