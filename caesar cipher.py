alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]

def encryption(plain_text, shift_text):
    cipher_text = ""
    for char in plain_text:

        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_text)%26
            cipher_text += alphabet[new_position]
        else:

            cipher_text += char
    print(f"Here is the text after encryption: {cipher_text}")

def decryption(cipher_text, shift_text):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_text)%26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the text after decryption: {plain_text}")

what_to_do = input("Type 'encrypt' for encryption, type 'decrypt' for decryption: \n").lower()

text = input("Type your message: ").lower()
shift = int(input("Type the shift value: "))


text = text.strip()

if what_to_do == "encrypt":
    encryption(plain_text=text, shift_text=shift)
elif what_to_do == "decrypt":
    decryption(cipher_text=text, shift_text=shift)