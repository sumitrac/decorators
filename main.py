def check_for_zero(operator):
    def wrapper(num1,num2):
        if num2 == 0:
          return "Cannot divide by zero."
        return operator 
    return wrapper


def sanitize(operator):
    def wrapper(num1,num2):
        if type(num1) == str and num1.isnumeric(): # isnumeric()
            num1 = int(num1)
        if type(num2) == str and num2.isnumeric(): # isnumeric()
            num2 = int(num2)
        operator(num1,num2)
    return wrapper

@sanitize 
def add(num1,num2):
    return num1 + num2

@sanitize
def subtract(num1,num2):
    return num1 - num2

@sanitize
@check_for_zero
def divide(num1,num2):
    return num1 / num2

print(add("3",2))
print(divide("3",0))
print(subtract(45,17))