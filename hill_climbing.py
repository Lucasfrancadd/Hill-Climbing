def hill_climbing(numeros, posicao_inicial):
    posicao = posicao_inicial

    while True:
        melhor_posicao = posicao

        if posicao > 0:
            if numeros[posicao - 1] > numeros[melhor_posicao]:
                melhor_posicao = posicao - 1

        
        if posicao < len(numeros) - 1:
            if numeros[posicao + 1] > numeros[melhor_posicao]:
                melhor_posicao = posicao + 1

        
        if melhor_posicao == posicao:
            break

        posicao = melhor_posicao

    return numeros[posicao]



numeros = [3, 8, 15, 10, 6, 20, 12, 7, 5, 18]

print("Lista de números:", numeros)

posicao_inicial = int(input("Digite a posição inicial (0 a 9): "))


if posicao_inicial < 0 or posicao_inicial >= len(numeros):
    print("Posição inválida!")
else:
    resultado = hill_climbing(numeros, posicao_inicial)
    print("Resultado do Hill Climbing:", resultado)
