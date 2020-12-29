def computePay(hours, rate):
    if hours > 40 :
        overtimeHours = hours - 40
        overtimeRate = rate * 1.5        
        pay =  (40 * rate) + (overtimeHours * overtimeRate)
    else :
        pay = hours * rate

    return pay

# strHours = input('Enter Hours: ')
# strRate = input('Enter Rate: ')
#floatHours = float(strHours)
# floatRate = float(strRate)

floatHours = float(input('Enter Hours: '))
floatRate = float(input('Enter Rate: '))

xp = computePay(floatHours, floatRate)

print('Pay:', xp)