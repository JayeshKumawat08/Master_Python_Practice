with open("top_secret.txt","w") as file:
    file.write("Quantum")

with open("top_secret.txt","rb") as file: 
    raw_bytes = file.read()

editable_bytes =  bytearray(raw_bytes)

print(f"Raw  Bytes Object : {raw_bytes}")
print(f"Byte Array List : {list(editable_bytes)}")