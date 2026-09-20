import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
ALPHABET = alphabet.upper()
p_len = int(input("Enter the length of the password: "))
password = ''.join(random.choice(alphabet + ALPHABET + numbers + symbols) for _ in range(p_len))
print("Your password is:", password)