original_byte = ord('A')
quantum_key = 170 

#encryption using bitwise XOR
encrypted_byte = original_byte ^ quantum_key

#decryption 
decrypted_byte = encrypted_byte ^ quantum_key

print(f"Original_Byte : {original_byte} (Character: '{chr(original_byte)}')")
print(f"Encrypted_Byte : {encrypted_byte} (Character: '{chr(encrypted_byte)}')")
print(f"Decrypted_Byte : {decrypted_byte} (Character: '{chr(decrypted_byte)}')")