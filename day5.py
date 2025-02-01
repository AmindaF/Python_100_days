import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

print("Welcome to the Random Password Generator\n")
num_letters = int(input("How many letters do you need? : \n"))
num_numbers = int(input("How many numbers do you need? : \n"))
num_symbols = int(input("How many symbols do you need? : \n"))

password_list = []

for letter in range(1, num_letters + 1):
	password_list.append(random.choice(letters))
for number in range(1, num_numbers + 1):
	password_list.append(random.choice(numbers))
for symbo in range(1, num_symbols + 1):
	password_list.append(random.choice(symbols))
random.shuffle(password_list)

password = ''.join(password_list)
print(f"Your Password is {password}")