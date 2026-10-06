import hashlib
import os 
import binascii

print("Key Derviation Practice")

# human input 
correct_pass = "MySecrectValut2026Practice"
wrong_pass = "mySecrectValut2026Practice"  # just one lowercase and it becomes wrong.

#Salt
#random noise

salt = os.random(16) # 16 bytes random noise

# Cryptographic Streaching (KDF)
# hash the password 100000 times using SHA-256

correct_key = hashlib.pbkdf2_hmac(
    hash_name = 'sha256',
    password = correct_pass.encode('utf-8'),
    salt = salt ,
    iterations = 100000
)

wrong_key = hashlib.pbkdf2_hmac(
    hash_name = 'sha256',
    password = wrong_pass.encode('utf-8'),
    salt = salt,
    iteration = 100000
)

# convert the raw binary keys to readable hexadecimal strings to see them 
hex_correct = binascii.hexlify(correct_key).decode('utf-8')
hex_wrong = binascii.hexlify(wrong_key).decode('utf-8')

print(f"Correct Password  : {correct_pass}")
print(f"Resulting 256-bit : {hex_correct}\n")

print(f"Wrong Password    : {wrong_pass}")
print(f"Resulting 256-bit : {hex_wrong}\n")

if hex_correct != hex_wrong:
    print("🔒 ZERO-TRUST ACTIVATED: The keys do not match. The vault remains locked.")