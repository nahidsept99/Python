#Retreives employee's information and returns it
def employeeInfo (inFile, ID):
    inF = open(inFile, 'r+')
    content = inF.read()
    contentLines = content.split('\n')

    for lines in contentLines:
        line = lines.split(',')
        if ID in line:
            return line
        else:
            continue
        if ID not in content:
            print('ID not in employee file list')
    inF.close()


#Defines the entire hiring process, checks whether the employee is blacklisted or not
def hireProcess (inFile, outFile, info):
    inF = open(inFile, 'r+')
    content = inF.read()
    contentLines = content.split('\n')

    

    outF = open(outFile, 'r+')
    if info.split(',')[0] in outF.read():           #Checks to see if the hired employee's ID is in the previous employee file
        outFContent = outF.read().split('\n')


        for line in outFContent:                    #Running check to see if new employee can be hired
            if info.split(',')[0] == line.split(',')[0]:

                if line.split(',')[6] == 'fired':
                    print('Employee is blacklisted')
                    break

                elif line.split(',')[6] == 'lay off' or line.split(',')[6] == 'Quit':
                    inF.write(info)
                    print('Employee was not blacklisted. Employee hired')
                    inF.close()

                    outF.close()
                
                    outF = open(outFile, 'r')
                    content = outF.read()       #Reads the content and stores them in content
                    outF.close()
                    outF = open(outFile, 'w')            #Wipes content in the file to rewite with new information

                    for line in content.split('\n'):
                        lst = line.split(',')
                        if lst[0] != info.split(',')[0]:
                            outF.write(line)
                            outF.close()
                            break

    else:
        inF.write('\n' + info)
        print('Employee hired')
        inF.close()
    outF.close()



#Fires the employee and adds the status of how they left the company.
def fireProcess(inFile, outFile, info, reason):
    outF = open(outFile, 'a')
    inF = open(inFile)

    for line in inF.read().split('\n'):
        if info in line:
            firedInfo = line
            employeeInfo = firedInfo
    
    
    
    updatedInfo = firedInfo.split(',')
    updatedInfo.pop(6)
    updatedInfo.append(reason)
    outF.write(updatedInfo[0] + ',' + updatedInfo[1] + ',' + updatedInfo[2] + ',' + updatedInfo[3] + ',' + updatedInfo[4] + ',' + updatedInfo[5] + ',' + updatedInfo[6] + '\n')
    outF.close()

    inF.close()

    inF = open(inFile, 'r')
    content = inF.readlines()
    inF.close()
    inF = open(inFile, 'w')

    for line in content:
        if line.split(',')[0] != employeeInfo.split(',')[0]:
            inF.write(line)

    inF.close()


def checkEmployeeInfo(info):

    employeeInfo = info.split(',')
    departments = ['Accounting', 'Business', 'Development', 'Engineering', 'Human Resources', 'Legal', 'Marketing', 'Product Managment', 'Research and Development', 'Sales', 'Services', 'Support', 'Training']
    if len(employeeInfo[0]) != 4:
        print('Invalid ID, Re-Enter')
    elif len(employeeInfo[1]) > 20 or (employeeInfo[1][0] == ' ' or employeeInfo[1][-1] == ' '):
        print('Invalid First Name, Re-Enter')
    elif len(employeeInfo[2]) > 20 or (employeeInfo[2][0] == ' ' or employeeInfo[2][-1] == ' '):
        print('Invalid Last Name, Re-Enter')
    elif '@' not in employeeInfo[3]:
        print('Invalid email, Re-Enter')
    elif employeeInfo[4] != ('Male' or 'Female' or 'male' or 'female'):
        print('Invalid gender description, Re-Enter')
    elif 100000 < int(employeeInfo[6]) or 50000 > int(employeeInfo[6]):
        print('Invalid Salary input, Re-Enter')
    else:
        return True
        
def checkID(inFile, ID):
    inF = open(inFile)
    if ID in inF.read():
        return True
    else:
        return False
    

def promotion(inFile, info):
    inF = open(inFile, 'r')
    if info in inF.read():
        inF.seek(0)
        content = inF.read().split('\n')

        for line in content:
            employee = line.split(',')
            if info in line.split(','):
                employeeInfo = line.split(',')

                increase = int(input('How much should the employee pay be increased. Enter by what percent the employees pay should be increased.Minimum of 2%: '))
                currentPay = employeeInfo[6]
                increasedPay = str(int(currentPay) * (1 + (int(increase) / 100)))

                employeeInfo[6] = increasedPay
                updatedInfo = '{},{},{},{},{},{},{}'.format(employeeInfo[0],employeeInfo[1],employeeInfo[2],employeeInfo[3],employeeInfo[4],employeeInfo[5],employeeInfo[6])

                inF.close()
                
                inF = open(inFile)
                oldContent = inF.read().split('\n')
                inF.close()
                inF = open(inFile, 'w')

                for lines in oldContent:
                    if lines.split(',')[0] != employeeInfo[0]:
                        inF.write(lines + '\n')
                    else:
                        inF.write(updatedInfo + '\n')
                        print('Employee pay increased to {}'.format(increasedPay))
            else:
                continue
    else:
        print('Employee not in DataBase')


def update (fileName, employee, info, position):
    inF = open(fileName)
    content = inF.read()
    inF.close()

    for line in content.split('\n'):
        if employee in line.split(','):
            employeeInfo = line.split(',')
            print(employeeInfo)
        else:
            continue
    employeeInfo[position] = info

    inF = open(fileName)
    newContent = inF.read().split('\n')
    inF.close

    inF = open(fileName, 'w')

    for line in newContent:
        if employeeInfo[0] != line.split(',')[0]:
            inF.write(line + '\n')
        else:
            inF.write('{},{},{},{},{},{},{}\n'.format(employeeInfo[0],employeeInfo[1],employeeInfo[2],employeeInfo[3],employeeInfo[4],employeeInfo[5],employeeInfo[6]))

    inF.close()


def salaryReport(inFile, salaryRange):
    inF = open(inFile)
    content = inF.read().split('\n')
    inF.close()

    salaryMin = int(salaryRange.split(',')[0])
    salaryMax = int(salaryRange.split(',')[1])
    
    count = 0
    
    for line in content:
        if int(line.split(',')[6]) >= salaryMin and int(line.split(',')[6]) <= salaryMax:
            count += 1
        else:
            continue

    print('\nSalary Report: There are {} employees with a salary between the range {} to {}'.format(str(count), str(salaryMin), str(salaryMax)))

    return count


def departmentReport(infile, info):
    inF = open(infile)
    content = inF.read().split('\n')
    inF.close()
    content.pop()
    
    count = 0
    
    for line in content:
        if line.split(',')[5] == info:
            count += 1
        else:
            continue

    print('\nDepartment {} report: {} Employees are working in this department'.format(info,str(count)))

    return count


def genderReport(inFile, gender1, gender2):
    inF = open(inFile)
    content = inF.read().split('\n')
    inF.close()
    content.pop()
    
    maleCount = 0
    femaleCount = 0
    
    for line in content:
        if line.split(',')[4] == gender1:
            maleCount +=1
        elif line.split(',')[4] == gender2:
            femaleCount += 1
        else:
            continue

    print('\nGender report: \n\nMale Employees: {} \nFemale Employees: {}'.format(str(maleCount), str(femaleCount)))

    return (maleCount,femaleCount)


def previousCount(inFile, type1, type2, type3):
    inF = open(inFile)
    content = inF.read().split('\n')
    content.pop()
    inF.close()

    firedCount = 0
    layOffCount = 0
    quitCount = 0

    for line in content:
        print(line.split(','))
        if line.split(',')[6] == type1:
            firedCount += 1
        elif line.split(',')[6] == type2:
            layOffCount += 1
        elif line.split(',')[6] == type3:
            quitCount += 1


    print('\nPrevious Employee Status Report: \n\nFired Employees: {} \nLay Off employees: {} \nQuit Employees: {}'.format(str(firedCount), str(layOffCount), str(quitCount)))

    return (firedCount,layOffCount,quitCount)



    
    
    
    
    


    












    















    
