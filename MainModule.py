import BusinessModule

fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Employee.txt'

print('\nWelcome to the HR Employee Managing System\n')

x = '1'
while x != '0':
    y = str(input('''\nWhat would you like to do: \nCheck employee information (1) \nHire new employee (2) \nFire employee (3) \nPromote employee (4) \nChange employee information (5) \nGenerate report (6) \nEnd Program (0)\n'''))

    if y == '1':
        BusinessModule.checkInfo(x)

    elif y == '2':
        BusinessModule.hireEmployee(x)

    elif y == '3':
        BusinessModule.fireEmployee(x)

    elif y == '4':
        BusinessModule.promoteEmployee(x)

    elif y == '5':
        BusinessModule.updateInfo(x)

    elif y == '6':
        BusinessModule.reportMod(x)

    elif y == '0':
        print('\nEnd of program\n')
        break

