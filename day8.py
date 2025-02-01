alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
	encrypted_text = ""
	for char in text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = (position + shift) % 26
			encrypted_text += alphabet[new_position]
		else:
			encrypted_text += char
	return encrypted_text;

def decrypt(text, shift):
	decrypted_text = ""
	for char in text:
		if char in alphabet:
			position = alphabet.index(char)
			new_position = (position - shift) % 26
			decrypted_text += alphabet[new_position]
		else:
			decrypted_text += char
	return decrypted_text;



while True:
    direction = input("Enter 'encode' to encrypt, Enter 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        if direction == 'encode':
            text = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            ecrypted_message = encrypt(text, shift)
            print(ecrypted_message)
        elif direction == 'decode':
            text = input("Type your message:\n")
            shift = int(input("Type the shift number:\n"))
            decrypted_message = decrypt(text, shift)
            print(decrypted_message)
        break
    else:
        print("Thats not the answer i was looking for. Please type 'ECODE' or 'DECODE'.")