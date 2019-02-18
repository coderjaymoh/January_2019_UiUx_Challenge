# METOD 1
import random, string
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
print(x)

# METHOD 2
import random, string
y = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
print(y)

# METHOD 3
import string
from random import *
min_char = 8
max_char = 12
allchar = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
print "This is your password : ",password
