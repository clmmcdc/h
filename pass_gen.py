import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
char = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
ALPHABET = alphabet.upper()
all_char = alphabet + ALPHABET + num + char
p_len = int(input("Enter the length of the password: "))
if p_len < 4:
    print("Password length should be at least 4 characters.")
else:
    print("Generating password...")
pw = [random.choice(alphabet), random.choice(ALPHABET), random.choice(num), random.choice(char)]

for _ in range(p_len - 4):
    pw.append(random.choice(all_char))

random.shuffle(pw)
password = ''.join(pw)
print("Your password is:", password)