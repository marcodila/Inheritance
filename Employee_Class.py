class Employee:

    def __init__(self, employee_name, employee_number):
        
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    #Accessors and Mutators for employee name and number
    def get_employee_name(self):
        return self.__employee_name


    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name


    def get_employee_number(self):
        return self.__employee_number


    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number


class Production_Worker(Employee):

    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        
        Employee.__init__(self, employee_name, employee_number)
        
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    #Accessors and Mutators for shift # and pay rate
    def get_shift_number(self):
        return self.__shift_number


    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number


    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate


class Shift_Supervisor(Employee):

    def __init__(self, employee_name, employee_number, annual_salary, annual_bonus):
        
        Employee.__init__(self, employee_name, employee_number)
        
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus

    #Accessors and Mutators for salary and bonus
    def get_annual_salary(self):
        return self.__annual_salary


    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary


    def get_annual_bonus(self):
        return self.__annual_bonus


    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus
