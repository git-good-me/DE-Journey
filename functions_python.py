def say_name(name):
    print(f'Hello {name}')
say_name('Faiz')

def add_num(num1, num2):
    return num1 + num2
result = add_num(5, 7)
print(f'The result is {result}')

def check_even_list(num_list):
    even_numbers = []
    for num in num_list:
        if num % 2 ==0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers
print(check_even_list([1,2,3,4,5,6,7,8,9,10]))

def employee_check(work_hours):

    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    return (employee_of_the_month, current_max)

print(employee_check([('John', 500), ('Bob', 600), ('Jane', 700)]))