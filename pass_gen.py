import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
ALPHABET = alphabet.upper()
print("Welcome to the Password Generator!")
input_length = int(input("Enter the desired length of your password: "))
password = ''.join(random.choice(alphabet + ALPHABET + numbers + symbols) for _ in range(input_length))
print("Your generated password is:", password)