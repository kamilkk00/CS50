from validator_collection import validators, checkers, errors

x = input("Email: ")
try:
    email_address = validators.email(x)
    is_email_address = checkers.is_email(x)
    print ("Valid")
except errors.InvalidEmailError:
    print ("Invalid")
except errors.EmptyValueError:
    print ("Invalid")
