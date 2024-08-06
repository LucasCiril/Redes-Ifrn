message = input("Digite a mensagem a ser criptografada: ")
key = input("Digite a chave para a cifra de Vigenère: ")

message = ''.join(filter(str.isalpha, message)).upper()
key = ''.join(filter(str.isalpha, key)).upper()

key = (key * (len(message) // len(key) + 1))[:len(message)]

encrypted_message = []
decrypted_message = []

for i in range(len(message)):
    t_val = ord(message[i]) - ord('A')
    k_val = ord(key[i]) - ord('A')
    c_val = (t_val + k_val) % 26
    encrypted_message.append(chr(c_val + ord('A')))

for i in range(len(encrypted_message)):
    c_val = ord(encrypted_message[i]) - ord('A')
    k_val = ord(key[i]) - ord('A')
    t_val = (c_val - k_val + 26) % 26
    decrypted_message.append(chr(t_val + ord('A')))

encrypted_message = ''.join(encrypted_message)
decrypted_message = ''.join(decrypted_message)

print(f"Mensagem criptografada: {encrypted_message}")
print(f"Mensagem descriptografada: {decrypted_message}")