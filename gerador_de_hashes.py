import hashlib

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH ###
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
    Digite o número do hash a ser gerado: '''))
print("-"*60)

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(f"O hash (md5) da string é: {resultado.hexdigest()}")
    print("-"*60)
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(f"O hash (sha1) da string é: {resultado.hexdigest()}")
    print("-"*60)
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(f"O hash (sha256) da string é: {resultado.hexdigest()}")
    print("-"*60)
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(f"O hash (sha512) da string é: {resultado.hexdigest()}")
    print("-"*60)
else:
    print("Digite um número de opção válido.")
    print("Encerrando programa...")
    print("-"*60)