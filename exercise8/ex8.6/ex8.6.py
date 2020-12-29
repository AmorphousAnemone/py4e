# Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when
# the user enters "done". Write the program to store the numbers the user
# enters in a list and use the max() and min() function to compute
# the maximum and minimum numbers after the loop completes.

numlist = list()
while(True):
    ninput = input('Enter a number: ')
    if ninput == 'done' or ninput == 'Done':
        break
    try:
        finput = float(ninput)
    except:
        print('Not a number')
        continue

    numlist.append(finput)

print('Maximum: ' + str(max(numlist)))
print('Minimum: ' + str(min(numlist)))

    # numlist.append(finput)