input_data = "QPSUJPO WJDJPVT QSJPSJUZ UXJDF"

def decode_caesar_cipher(data, shift):
    decoded = ""
    for char in data:
        if char.isalpha():
            # Shift character and wrap around alphabet
            shifted = chr((ord(char) - shift - 65) % 26 + 65)
            decoded += shifted
        else:
            decoded += char
    return decoded


if __name__ == "__main__":
    for i in range(26):
        print(decode_caesar_cipher(input_data, -i))