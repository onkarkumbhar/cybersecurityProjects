# /bin/python3
# Command Line Tool
import random

l = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
n = list("0123456789")
s = list("!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~")

wish = int(input("Enter password length: "))
if wish<6:
    print("Password should be greater than atleast 6 letters")
    exit()

passw = ""

for j in range(wish-4):
    rand_idx = random.randrange(len(l))
    passw += l[rand_idx]
w = random.randint(0,wish-4)
passw[w].upper()
for k in range(wish-4,wish-2):
    rand_idx = random.randrange(len(n))
    passw += n[rand_idx]
for z in range(wish-2,wish):
    rand_idx = random.randrange(len(s))
    passw += s[rand_idx]
print(passw)
