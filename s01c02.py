def fixed_xor(hex_string1, hex_string2):
    bytes1 = bytes.fromhex(hex_string1)
    bytes2 = bytes.fromhex(hex_string2)

    xored_bytes = bytes(x ^ y for x, y in zip(bytes1, bytes2))
    
    return xored_bytes.hex()


hex_string1 =input("enter a hex number 1 : ")
hex_string2 =input("enter a hex number 2 : ")

result = fixed_xor(hex_string1, hex_string2)

print("XOR result : ", result)
