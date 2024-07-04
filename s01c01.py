import base64

def hex_to_base64(hex_string):
    byte_data = bytes.fromhex(hex_string)
    base64_encoded_bytes = base64.b64encode(byte_data)
    return base64_encoded_bytes.decode('utf-8')


hex_input = input("Enter a hexadecimal string: ")

base64_output = hex_to_base64(hex_input)


print("Base64 encoded:", base64_output)
