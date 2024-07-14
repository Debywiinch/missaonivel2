# Entrada de dados
dados = [1, 2, 3]

# Cálculos intermediários
def calcular_subconjuntos(dados):
    subconjuntos = [[]]
    for elemento in dados:
        for subconjunto in subconjuntos.copy():
            novo_subconjunto = subconjunto + [elemento]
            subconjuntos.append(novo_subconjunto)
    return subconjuntos

# Apresentação dos resultados
def apresentar_resultados(subconjuntos):
    for subconjunto in subconjuntos:
        print(subconjunto)

# Execução do teste
subconjuntos = calcular_subconjuntos(dados)
apresentar_resultados(subconjuntos)