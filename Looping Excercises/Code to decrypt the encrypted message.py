#Programming code to decrypt the encrypted message to get the original one, using loop ..
#encryption using the ascii code
#ord() function returns the Unicode code from a given character.
#......................................................................
msg = input("Enter a message to decrypt: ")
encmsg = ""

for ch in msg:
    asc = ord(ch) - 3
    ench = chr(asc)
    encmsg += ench
print("Decrypted message:",encmsg)