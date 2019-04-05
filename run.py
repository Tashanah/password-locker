import random
import string



def randomStringDigits(stringLength=6):
    password=string.ascii_letters + string.digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
print (randomStringDigits(12))


