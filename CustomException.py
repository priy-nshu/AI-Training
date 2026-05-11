class CustomError(Exception):
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Negative value is not allowed.")
    
def RaiseExcep():
    try:
        check_value(-5)
    except CustomError as e:
        print(f'Caught CustomError: {e}')
        
RaiseExcep()