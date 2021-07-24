import random
len = int(input("Enter the length of the password : "))
string = 'abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$&*()_-'
print("".join(random.sample(string, len)))