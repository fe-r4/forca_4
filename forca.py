import random

# Lista de palavras
palavras = ["python", "programacao", "jogo", "forca", "desenvolvimento"]

# Escolha aleatória de palavra
palavra = random.choice(palavras)
letras_corretas = ["_"] * len(palavra)
tentativas = 6
letras_erradas = []

print("Bem-vindo ao Jogo da Forca!")
print("Você tem 6 tentativas para adivinhar a palavra.")

while tentativas > 0 and "_" in letras_corretas:
    print("\nPalavra:", " ".join(letras_corretas))
    print(f"Tentativas restantes: {tentativas}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in palavra:
        for idx, char in enumerate(palavra):
            if char == letra:
                letras_corretas[idx] = letra
        print("Boa! Letra correta!")
    else:
        tentativas -= 1
        letras_erradas.append(letra)
        print("Ops! Letra incorreta.")
    
if "_" not in letras_corretas:
 print("\nParabéns! Você venceu!")
    print(f"A palavra era: {palavra}")
else:
    print("\nVocê perdeu! Suas tentativas acabaram.")
    print(f"A palavra era: {palavra}")
