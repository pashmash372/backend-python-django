from datetime import datetime


def log_datetime(func): # define the decorator function
    '''log the date and time of a function'''
    print("Inside log date time")
    def wrapper(): # define the wrapper function
        print(f'Function: \n Run on {datetime.today().strftime("%d-%m-%Y %H:%M:%S")}') # print the date and time
        print(f'{"-" * 50}') # print 50 dashes
        # func("Executing func") # run the function
        func() # run the function
        return "Done executing wrapper function"
    print("Wrapper function defined,now going to return")
    return wrapper # return the wrapper function


def measure_performance(func): # define the decorator function
    def wrapper(*args,**kwargs):
        start_time=datetime.now()
        func(*args,**kwargs) # run the function
        end_time=datetime.now()
        delta = end_time - start_time
        print(f"Time taken to execute {func.__name__} is {delta}")
        return "Done executing wrapper function"
    print("Wrapper function defined,now going to return")
    return wrapper # return the wrapper function
