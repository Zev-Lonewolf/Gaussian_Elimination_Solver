def print_matriz(matriz):
    for linha in matriz:
        print(linha)
    print()

def escalonar(matriz):
    n = len(matriz)
    for i in range(n):
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break
        pivô = matriz[i][i]
        for j in range(i + 1, n):
            fator = matriz[j][i] / pivô
            for k in range(i, n + 1):
                matriz[j][k] -= fator * matriz[i][k]
    return matriz

def retro_substituicao(matriz):
    n = len(matriz)
    solucoes = [0] * n
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matriz[i][j] * solucoes[j]
        solucoes[i] = (matriz[i][n] - soma) / matriz[i][i]
    return solucoes

def main():
    n = int(input("Quantas variáveis tem o sistema? "))
    matriz = []

    print(f"\nDigite os coeficientes da matriz aumentada (linha por linha, incluindo os resultados):")
    for i in range(n):
        linha = list(map(float, input(f"Linha {i + 1}: ").split()))
        while len(linha) != n + 1:
            print("Quantidade incorreta de valores. Tente novamente.")
            linha = list(map(float, input(f"Linha {i + 1}: ").split()))
        matriz.append(linha)

    print("\nMatriz original:")
    print_matriz(matriz)

    escalonada = escalonar(matriz)

    print("Matriz escalonada:")
    print_matriz(escalonada)

    solucao = retro_substituicao(escalonada)

    print("Soluções encontradas:")
    for i, valor in enumerate(solucao):
        print(f"x{i + 1} = {valor:.2f}")

main()
