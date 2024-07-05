def repeating_key_xor(plaintext, key):
    ciphertext = ""
    key_length = len(key)

    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % key_length]))

    return ciphertext.encode().hex()

plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
ciphertext = repeating_key_xor(plaintext, key)
print(ciphertext)
