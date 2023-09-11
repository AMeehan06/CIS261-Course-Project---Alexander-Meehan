from datetime import datetime

def CreateUsers():
    print("Creat users, passwords, and roles")
    UserFile = open("users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter a username or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter a role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter a user role (Admin or User): ")
            
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)
        
def Login():
    UserFile = open("Users.txt", "r")
    UserList = []
    UserName = input("Enter username: ")
    UserPwd = input("Enter password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
            UserRole = UserList[2]
            return UserRole, UserName

    return UserRole, UserName

def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getDatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter the end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate

def getHoursWorked():
    hours = float(input("Enter the amount of hours worked: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (mm/dd/yyyy) or ALL for all data: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again. ") 
            print()
            continue
        
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        EmpList = EmpDetail.split("|")
        fromDate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromDate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        endDate = EmpList[1]
        empName = EmpList[2]
        hours = float(EmpList[3])
        hourlyRate = float(EmpList[4])
        taxRate = float(EmpList[5])
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay
        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
        DetailsPrinted = True
        
    if (DetailsPrinted):
        printTotals(empTotals)
    else:
        print("No detailed information to print")
        
def printTotals(empTotals):
    print(f'Total number of employees: {empTotals["totEmp"]}')
    print(f'Total number of hours worked: {empTotals["totHours"]:,.2f}')
    print(f'Total Gross Pay: {empTotals["totGross"]:,.2f}')
    print(f'Total Tax: {empTotals["totTax"]:,.1%}')
    print(f'Total Net Pay of Employees: {empTotals["totNet"]:,.2f}')
             
if __name__ == "__main__":
    CreateUsers()
    print()
    print("Data Entry")
    UserRole, UserName = Login()
    DetailsPrinted = False
    empTotals = {}
    if (UserRole.upper() == "NONE"):
        print(UserName, " is invalid.")
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                empName = getEmpName()
                if (empName.upper() == "END"):
                    break
                fromDate, endDate, = getDatesWorked()
                hours = getHoursWorked()
                hourlyrate = getHourlyRate()
                taxRate = getTaxRate()
                empDetail = fromDate + "|" + empName + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxRate) + "\n"
                EmpFile.write(empDetail)
                
            EmpFile.close()
            
        printInfo(DetailsPrinted)
      
     

  
