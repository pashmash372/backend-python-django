from my_library import log_datetime  # import the decorator

# print(log_datetime)
# log_datetime("random string")  # run the decorator
"""
OUTPUT for above code
<function log_datetime at 0x0000015C2EA7AEE0>
Inside log date time
Wrapper function defined,now going to return

"""

# wrapper_func= log_datetime("random string")  # run the decorator
# print(wrapper_func)
"""
output for above code
Inside log date time
Wrapper function defined,now going to return
<function log_datetime.<locals>.wrapper at 0x0000023500C7A0D0>
"""

# wrapper_func= log_datetime("random string")  # run the decorator
# print(wrapper_func())   # TypeError: 'str' object is not callable


wrapper_func= log_datetime(print)  # run the decorator
# print(wrapper_func())
print ("On line 11 inside my_library.py:",wrapper_func())

"""
Inside log date time
Wrapper function defined,now going to return
Function: 
 Run on 09-06-2023 23:05:26
--------------------------------------------------
Executing func
On line 11 inside my_library.py: Done executing wrapper function
"""




