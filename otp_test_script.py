# mini quantum seeded otp test script
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
txt_path = os.path.join(BASE_DIR, "top_secret.txt")
bin_path = os.path.join(BASE_DIR, "encrypted_secret.bin")
key_byte = 170
print("encrpytion phase")

with open(txt_path,"rb") as file:
    file_bytes = bytearray(file.read())

for i in range(len(file_bytes)):
    file_bytes[i] = file_bytes[i] ^ key_byte

with open(bin_path,"wb") as file:
    file.write(file_bytes)

print("Successfully encrypted into 'encrypted_secrets.bin'")

print("\n\nDecryption Phase ")

with open(bin_path,"rb") as file:
    encrypted_bytes = bytearray(file.read())

for i in range(len(encrypted_bytes)):
    encrypted_bytes[i] = encrypted_bytes[i] ^ key_byte

decrypted_text = encrypted_bytes.decode('utf-8')
print(f"Decrypted Data: {decrypted_text}")
