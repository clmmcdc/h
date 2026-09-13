data = input("Enter data: ")
d1 = data.find("|")
name = data[:d1].strip().title()
dname = name.upper()
name_len=len(name)
d2 = data.find("|", d1 + 1)
character = data[d1 + 1:d2].strip().upper()
cha_len = len(character)
d3 = data.find("|", d2 + 1)
city = data[d2 + 1:d3].strip().title()
d4 = data.find("|", d3 + 1)
scode = data[d3 + 1:d4].strip().upper()
d5 = data.find("|", d4 + 1)
quote = data[d4 + 1:d5].strip().upper()
firstname_char = character[:6]
lastname_char = character[6:]
year = scode[2:6]
code = scode[6:] 
skill = (code + " ") * 3
n1 = name.find(" ")
fn = name[:n1].strip().title()
n2 = name.find(" ", n1 + 1)
ln = name[n1 + 1:n2].strip().title()
n3 = name.find(" ", n2 + 1)
tn = name[n2 + 1:n3].strip().title()
tag = f"{fn[0]}{ln[0]}{tn[0]}_{character}"

WIDTH = 41

top_border    = f"╔{'═' * WIDTH}╗"
mid_border    = f"╠{'═' * WIDTH}╣"
bottom_border = f"╚{'═' * WIDTH}╝"

def print_empty():
    print(f"║{' ' * WIDTH}║")

def print_center(text):
    print(f"║{text:^{WIDTH}}║")

def print_left(text):
    print(f"║ {text:<{WIDTH - 1}}║")

print(top_border)
print_center("CHARACTER DATABASE")
print(bottom_border)
print_empty()

print_left("PLAYER:")
print_left(f"{name}")
print_empty()

print_left("DISPLAY NAME:")
print_left(f"{dname}")
print_empty()

print_left("CHARACTER:")
print_left(f"{character}")
print_empty()

print_left("CITY:")
print_left(f"{city}")
print_empty()

print(top_border)
print_center("STATISTICS")
print(bottom_border)

print_left(f"Player length: {name_len}")
print_left(f"Character length: {cha_len}")
print_left(f"Character first name: {firstname_char}")
print_left(f"Character last name: {lastname_char}")
print_empty()

print_left(f"Year: {year}")
print_left(f"Code: {code}")
print_empty()

print_left("PLAYER TAG: ")
print_left(f"{tag}")
print_empty()

print_left("QUOTE: ")
print_left(f"\"{quote}\"")
print_empty()

print_left("SKILL: ")
print_left(f"{skill}")
print(bottom_border)
