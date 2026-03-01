from Employee_Class import Production_Worker

#User Input
name = input("Enter employee name: ")
number = input("Enter employee number: ")
shift = input("Enter shift number: ")
pay_rate = input("Enter hourly pay rate: ")

#Production Worker Object
worker = Production_Worker(name, number, shift, pay_rate)

print("\n--- Employee Information ---")
print("Employee Name:    ", worker.get_employee_name())
print("Employee Number:  ", worker.get_employee_number())
print("Shift Number:     ", worker.get_shift_number())
print("Hourly Pay Rate: $", worker.get_hourly_pay_rate(), sep="")
