import random
import string

def generate_password(length=12):
    characters =string.digits +string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
password = generate_password()
print("Generated Password:", password)

