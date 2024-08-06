import os

PALAVRA_CHAVE = "uniaoflasco"

palavra_oculta = ["_" for _ in PALAVRA_CHAVE]
letras_erradas = []
tentativas_restantes = 6

while tentativas_restantes > 0 and "_" in palavra_oculta:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Palavra: " + " ".join(palavra_oculta))
    print("Letras erradas: " + " ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    tentativa = input("Digite uma letra: ").lower()
    
    if tentativa in letras_erradas or tentativa in palavra_oculta:
        print("Você já tentou essa letra. Tente outra.")
        continue
    
    if tentativa in PALAVRA_CHAVE:
        for i, letra in enumerate(PALAVRA_CHAVE):
            if letra.lower() == tentativa:
                palavra_oculta[i] = letra
    else:
        letras_erradas.append(tentativa)
        tentativas_restantes -= 1

os.system('cls' if os.name == 'nt' else 'clear')
print("Palavra: " + " ".join(palavra_oculta))
print("Letras erradas: " + " ".join(letras_erradas))
print(f"Tentativas restantes: {tentativas_restantes}")

if "_" not in palavra_oculta:
    print("Parabéns! Você acertou a palavra.")
else:
    print(f"Você perdeu. A palavra era '{PALAVRA_CHAVE}'.")