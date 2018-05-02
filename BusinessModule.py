import DataModule

def checkInfo(x):                 #Check the file and print out the employee's information
    fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Employee.txt'

    info = str(input('How would you like to check the employee\'s info: ID (1), First Name (2), Last Name (3), or Email (4): '))

    if info == '1':
        ID = str(input('Enter ID: '))
        print(DataModule.employeeInfo(fileName, ID))
    elif info == '2':
        ID = str(input('Enter First Name: '))
        print(DataModule.employeeInfo(fileName, ID))
    elif info == '3':
        ID = str(input('Enter Last Name: '))
        print(DataModule.employeeInfo(fileName, ID))
    elif info == '4':
        ID = str(input('Enter Email: '))
        print(DataModule.employeeInfo(fileName, ID))
    else:
        print ('Invaild Input')

    
def hireEmployee (info):
    fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Employee.txt'
    fileName2 =  'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Previous_Employee.txt'

    while True:
        info = str(input('Enter the new employee\'s in the format id,first_name,last_name,email,gender,department,Salary: '))
        if DataModule.checkEmployeeInfo(info):
            DataModule.hireProcess(fileName, fileName2, info)
            break
        else:
            print('Re-Enter your information')
            continue

    
def fireEmployee (x):
    fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Employee.txt'
    fileName2 =  'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Previous_Employee.txt'

    info = str(input('\nEnter one of the following for the employee being fire: ID, First Name, Last Name, or Email: '))
    fReason = str(input('Enter the reason for being fired: Fired (1), Layed off (2), Quit (3): '))

    if fReason == '1':
        reason = 'Fired'
    elif fReason == '2':
        reason = 'Lay off'
    elif fReason == '3':
        reason = 'Quit'
    else:
        print('Invalid input')
    

    DataModule.fireProcess(fileName, fileName2, info, reason)

    print('Employee removed from List')


def promoteEmployee(x):
    fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Employee.txt'
    info = str(input('\nEnter one of the following for the employee being promoted: ID, First Name, Last Name, or Email: '))
    DataModule.promotion(fileName, info)


    
def updateInfo(x):
    fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Employee.txt'
    employee = str(input('\nEnter one of the following for the employee whose information is being updated: ID, First Name, Last Name, or Email: '))
    section = str(input('Enter which of the following needs to be changed: First Name (1), Last Name (2), Email (3), Department (4), Salary (5)'))

    y = True
    while y == True:
        if section == '1':
            position = 1
            info = str(input('Enter the updated First Name: '))
            if len(info) > 20 and (info[0] == ' ' or info[-1] == ' '):
                print('Invalid First Name: Re-Enter')
                continue
            else:
                break

        elif section == '2':
            position = 2
            info = str(input('Enter the updated Last Name: '))
            if len(info) > 20 and (info[0] == ' ' or info[-1] == ' '):
                print('Invalid Last Name: Re-Enter')
                continue
            else:
                break

        elif section == '3':
            position = 3
            info = str(input('Enter the new Email: '))
            if  '@' not in info:
                print('Invalid email, Re-Enter')
                continue
            else:
                break

        elif section == '4':
            department = int(input('Enter the new department: Accounting(1), Business(2), Development(3), Engineering(4), Human Resources(5), Legal(6), \nMarketing(7), Product Managment(8), Research and Development(9), Sales(10), Services(11), Support(12), Training(13)'))
            position = 5
            if department == 1:
                info = 'Accounting'
                break          
            elif department == 2:
                info = 'Business'
                break
            elif department == 3:
                info = 'Development'
                break
            elif department == 4:
                info = 'Engineering'
                break
            elif department == 5:
                info = 'Human Resources'
                break
            elif department == 6:
                info = 'Legal'
                break
            elif department == 7:
                info = 'Marketing'
                break
            elif department == 8:
                info = 'Product Managment'
                break
            elif department == 9:
                info = 'Research and Development'
                break
            elif department == 10:
                info = 'Sales'
                break
            elif department == 11:
                info = 'Services'
                break
            elif department == 12:
                info = 'Support'
                break
            elif department == 13:
                info = 'Training'
                break
            else:
                print('Invalid input. Enter Again')
                continue

        
        elif section == '5':
            position = 6
            info = str(input('Enter the new salary for the employee'))
            if salary > '100000' or salary < '50000':
                print('Invalid salary entered. Please re-enter')
                continue
            else:
                break

        else:
            print('Invalid Input')
            section = str(input('Re-Enter which of the following needs to be changed: First Name (1), Last Name (2), Email (3), Department (4), Salary (5)'))
            continue

    DataModule.update(fileName, employee, info, position)

    print('Info updated')

    

def reportMod(x):
    fileName = 'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Employee.txt'
    fileName2 =  'C:/Users/nahid.DESKTOP-S18FO6A/Desktop/Final Project/Previous_Employee.txt'
    
    reportType = int(input('What type of report would you like to generate: \n\n(1) Salary Range of Workers \n(2) Head Count in a Department \n(3) Gender \n(4) Employees that left the company\n'))

    while True:
        if reportType == 1:
            #Report by determining the amount of employees that fall in a salary range
            salaryRange = int(input('Enter the salary range in the format (min,max): '))

            if int(salaryRange.split(',')[0]) < 0 or int(salaryRange.split(',')[1]) > 100000 or int(salaryRange.split(',')[0]) > 100000 or int(salaryRange.split(',')[1]) < 0:
                print('Invalid range entered. Please re-enter the range.')
                continue
            else:
                DataModule.salaryReport(fileName,salaryRange)
                break

            #End
            
        elif reportType == 2:
            #Report Separator By Department
            department = int(input('Enter the department to report on: \n\nAccounting(1) \nBusiness(2) \nDevelopment(3) \nEngineering(4) \nHuman Resources(5) \nLegal(6) \nMarketing(7) \nProduct Managment(8) \nResearch and Development(9) \nSales(10) \nServices(11) \nSupport(12) \nTraining(13) \nQuit(0)\n'))

            if department == 1:
                info = 'Accounting'
                DataModule.departmentReport(fileName, info)
                break          
            elif department == 2:
                info = 'Business'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 3:
                info = 'Development'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 4:
                info = 'Engineering'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 5:
                info = 'Human Resources'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 6:
                info = 'Legal'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 7:
                info = 'Marketing'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 8:
                info = 'Product Managment'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 9:
                info = 'Research and Development'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 10:
                info = 'Sales'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 11:
                info = 'Services'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 12:
                info = 'Support'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 13:
                info = 'Training'
                DataModule.departmentReport(fileName, info)
                break
            elif department == 0:
                break
            else:
                print('Invalid input. Enter Again')
                continue

            

            #End
            
        elif reportType == 3:
            #Report generating the number of males and females in the company
            
            type1 = 'Male'
            type2 = 'Female'

            DataModule.genderReport(fileName, type1, type2)
            
            break
            


        elif reportType == 4:
            type1 = 'Fired'
            type2 = 'Lay off'
            type3 = 'Quit'
            
            DataModule.previousCount(fileName2, type1, type2, type3)
            
            break

        else:
            print('Invalid Input. Please Re-Enter.')
            reportType = int(input('\nWhat type of report would you like to generate: \n\n(1) Salary Range of Workers \n(2) Head Count in a Department \n(3) Gender \n(4) Blacklisted Employee Count \n(5) Lay Off Employee Count \n(6) Employee Quit Count\n'))
            continue

    print('\nReport Generated')


            
            
        




























