from Employee_Class import Shift_Supervisor

#User Input
name = input("Enter employee name: ")
number = input("Enter employee number: ")
salary = input("Enter annual salary: ")
bonus = input("Enter annual bonus: ")

#Shift Supervisor Object
supervisor = Shift_Supervisor(name, number, salary, bonus)

print("\n--- Supervisor Information ---")
print("Employee Name:   ", supervisor.get_employee_name())
print("Employee Number: ", supervisor.get_employee_number())
print("Annual Salary:  $", supervisor.get_annual_salary(), sep="")
print("Annual Bonus:   $", supervisor.get_annual_bonus(), sep="")
