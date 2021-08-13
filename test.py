from model import Employee
import operations as empopr
print('-'*8,'Welcome To Employee Record Management System','-'*8)
#Here we are doing menu based programminng
choice = 0
while(choice!=5):
    print('1-Add new Employee')
    print('2-Show Employee')
    print('3-Delete Employee')
    print('4-Update Employee')
    print('5-Exit')
    choice = int(input('Enter your choice '))

    if choice == 1:
        _id = int(input('Enter Employee Id '))
        name = input('Enter Employee Name ')
        sal = float(input('Enter Employee Salary '))

        #Now will create obj of Employee with some details
        empobj = Employee(_id,name,sal)
        msg = empopr.addEmp(empobj)
        print(msg,end='\n\n')

    elif choice == 2:
        empopr.showEmps()

    elif choice == 3:
        _id = int(input('Enter Employee Id to delete '))
        msg = empopr.deleteEmp(_id)
        print(msg,end='\n\n')

    elif choice == 4:
        _id = int(input('Enter Employee Id to update '))
        name = input('Enter Employee Updated name ')
        sal = float(input('Enter Employee updated salary '))
        empobj = Employee(_id,name,sal)
        msg = empopr.updateEmp(_id,empobj)
        print(msg,end='\n\n')

    elif choice == 5:
        print('Good Bye.....')

    else:
        print('Invalid choice') 


