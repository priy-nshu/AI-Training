def MultiException():
    try:
        result=int("abc")
        # This will raise VAlueError
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError as e:
        print(f'Caught ValueError: {e}')

def check_positive(x):
    if x < 0:
        raise ValueError("Negative value is not allowed.")
    return x
def RaiseException():
    try:
        check_positive(-5)
    except ValueError as e:
        print(f'Caught ValueError: {e}')

a,b=4,0

def ExceptionHandling(a,b):
    try:
        result=a/b
    except ZeroDivisionError as e:
        print(f'Caught ZeroDivisionError: {e}')
    else:
        print(f'The result is: {result}')
    finally:
        print("This block will always execute.")

def AssertRaise():
    assert b != 0, "Denominator cannot be zero."
    print("Assertion passed.")
    
#########################################################
MultiException()
#check_positive(-5)
RaiseException()
ExceptionHandling(a,b)
AssertRaise()