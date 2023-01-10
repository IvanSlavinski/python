import random
import time

pass_values = list("QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp0123456789")
password = str(input('Enter your password: '))


while True:
    password_key_gen = ''
    while len(password_key_gen) < len(password):
        x = random.choice(pass_values)
        password_key_gen += str(x)
    if password_key_gen == password:
        print(f"Your password is {password}. The computer generated equal password {password_key_gen}.")
        print(f'It took {time.process_time()} to generate the password.')
        break
    else:
        continue
