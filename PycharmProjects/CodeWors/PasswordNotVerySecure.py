# At least one character ("" is not valid)
# Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
# No whitespaces / underscore
import re
def alphaNumaric(password):
    wout = re.sub(r'[^0-9a-zA-Z]','', password)
    print("within -->", password)
    print("without --> ", wout)

    return True if password == wout else False


print(alphaNumaric("passw45-ord"))

# II.yol
def alphanumeric(password):
    return password.isalnum()

print(alphanumeric("dssfadfa+"))