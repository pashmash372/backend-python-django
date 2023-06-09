def my_email_function(sender_email_address, subject, message):
    print(f"Sending email from {sender_email_address} with subject {subject} and message {message}")
    return True


def my_email_function(sender_email_address, subject, message, cc_email):
    print(f"Sending email from {sender_email_address} with subject {subject} and message {message}")
    print(f"CC email address is {cc_email}")
    return True


# Option two - add a default value to the argument
def my_email_function(sender_email_address, subject, message, cc_email=None): #problem with this is that if we want to send email to multiple people, we cannot do that
    print(f"Sending email from {sender_email_address} with subject {subject} and message {message}")
    if cc_email is not None:
        print(f"CC email option is {cc_email}")
    return True


# Option three - use kwargs as cc_email
def my_email_function(sender_email_address,subject,message,**kwargs): # problem with this is that we can send any number of arguments
    print(f"Sending email from {sender_email_address} with subject {subject} and message {message}")
    if 'cc_email' in kwargs:
        print(f"CC email option is {kwargs['cc_email']}") # kwargs['cc_email'] is same as kwargs.get('cc_email')
        # cannot use double quotes in kwargs.get("cc_email") as it will be considered as string

    return True


# why use kwargs - backward compatibility
# why use kwargs - variable length arguments
# why use kwargs - order does not matter
# why use kwargs - dictionary - key value pair
# why use kwargs - default value
# why use kwargs - multiple arguments
