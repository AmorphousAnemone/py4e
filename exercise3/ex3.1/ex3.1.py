strHours = input('Enter Hours: ')
strRate = input('Enter Rate: ')

floatHours = float(strHours)
floatRate = float(strRate)

if floatHours > 40 :
    overtimeHours = floatHours - 40
    overtimeRate = floatRate * 1.5
    # print('')
    # print('Overtime hours: ' + str(overtimeHours))
    # print('Overtime rate: ' + str(overtimeRate))

    xp = (40 * floatRate) + (overtimeHours * overtimeRate)

else :
    # print('Regular')
    xp = floatHours * floatRate

print('Pay:', xp)