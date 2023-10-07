#Random password generator in python
#importing random and string modules
import random
import string

print("Welcome to password generator in python!!!")
len=int(input("Enter the length of password : "))

#define data
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbols=string.punctuation

all=lower+upper+num+symbols
# use random
temp=random.sample(all,len)
#convert into string
password="".join(temp)

print(password)