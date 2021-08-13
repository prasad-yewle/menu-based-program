from model import Employee
# It is empty list of employee obj
emplist = []

#It is functn which used to add obj into emplist
def addEmp(empobj):
    emplist.append(empobj)
    return 'Employee added successfully'

def showEmps():
    print('-*'*10,'Employee list','-*'*10)
    for emp in emplist:
        print(emp)
        print('_'*40)
    else:
        print('\n','-'*50)

def deleteEmp(_Id):
    for emp in emplist:
        if emp.empId == _Id:
            emplist.remove(emp)
            return f'Employee is deleted {emp}'

    else:
        return 'Employee id is not found...'

def updateEmp(_id,newempobj):
    for emp in emplist:
        if emp.empId == _id:
            emplist[emplist.index(emp)] = newempobj
            return f'Employee is updated as {newempobj}'
    else:
        return 'Employee Record Not Updated...'