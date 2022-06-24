import re

def is_email(email: str):
    return re.fullmatch("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$", email)

def generate_confirmation_code():
    code = ""
    for i in range(6):
        code += str(random.randint(0, 9))
    return int(code)
