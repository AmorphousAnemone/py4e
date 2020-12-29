# print('Five')

sum = 0
count = 0
avg = None
while True:
    val = input('Enter a number: ')
    if val == 'done':
        break
    try:    # val needs to be integer
        val = int(val)   
        # print(val) 
    except:
        print('Invalid input')
        continue
    count = count + 1
    sum = sum + val
    if count > 0:   # avoid undefined answer
        avg = sum / count
print(sum, count, avg)