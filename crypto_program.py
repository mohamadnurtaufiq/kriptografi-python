# Program Kriptografi Dasar
# Caesar Cipher dan Transposition Cipher

# =========================
# CAESAR CIPHER
# =========================

def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + key) % 26
            ciphertext += chr(shift + ord('a'))
        else:
            ciphertext += char
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') - key) % 26
            plaintext += chr(shift + ord('a'))
        else:
            plaintext += char
    return plaintext


# =========================
# TRANSPOSITION CIPHER
# =========================

def transposition_encrypt(plaintext, key):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key

    return ''.join(ciphertext)


def transposition_decrypt(ciphertext, key):
    num_cols = len(ciphertext) // key
    num_rows = key
    num_shaded_boxes = len(ciphertext) % key

    plaintext = [''] * num_cols

    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1

        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# =========================
# MENU PROGRAM
# =========================

print("PROGRAM KRIPTOGRAFI DASAR")
print("1. Caesar Cipher")
print("2. Transposition Cipher")

pilih = input("Pilih metode (1/2): ")

if pilih == "1":

    print("\nCAESAR CIPHER")
    mode = input("Pilih (e = enkripsi / d = dekripsi): ")
    text = input("Masukkan teks: ")
    key = int(input("Masukkan key (shift): "))

    if mode == "e":
        hasil = caesar_encrypt(text, key)
        print("Plaintext :", text)
        print("Ciphertext:", hasil)
        print("Key :", key)

    elif mode == "d":
        hasil = caesar_decrypt(text, key)
        print("Ciphertext:", text)
        print("Plaintext :", hasil)
        print("Key :", key)


elif pilih == "2":

    print("\nTRANSPOSITION CIPHER")
    mode = input("Pilih (e = enkripsi / d = dekripsi): ")
    text = input("Masukkan teks: ")
    key = int(input("Masukkan key: "))

    if mode == "e":
        hasil = transposition_encrypt(text, key)
        print("Plaintext :", text)
        print("Ciphertext:", hasil)
        print("Key :", key)

    elif mode == "d":
        hasil = transposition_decrypt(text, key)
        print("Ciphertext:", text)
        print("Plaintext :", hasil)
        print("Key :", key)

else:
    print("Pilihan tidak tersedia")