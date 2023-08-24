import string
import random 

def generate_senha(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password

password_length = int(input("Entre com o tamanho de senha desejada: "))

generated_password = generate_senha(password_length)

print("Senha Gerada: ", generated_password)