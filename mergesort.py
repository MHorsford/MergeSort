def merge_sort(arr: list, counter: list) -> list:
    """
    Merge Sort (recursivo)
    Ideia:
      1) Divide: separa a lista em duas metades
      2) Conquista: ordena recursivamente cada metade
      3) Combina: junta (merge) duas metades já ordenadas
    Medida de desempenho:
      - counter[0] soma 1 para cada linha/checagem executada (critério uniforme).
    """

    # --- Caso base: lista de tamanho 0 ou 1 já está ordenada ---
    counter[0] += 1  # conta a execução do IF (checagem do caso base)
    if len(arr) <= 1:
        counter[0] += 1  # conta o return do caso base
        return arr

    # --- DIVIDE: calcula o meio e cria as duas metades ---
    counter[0] += 1  # conta a atribuição do meio
    mid = len(arr) // 2

    counter[0] += 1  # conta a criação (fatiamento) da metade esquerda
    left_half = arr[:mid]

    counter[0] += 1  # conta a criação (fatiamento) da metade direita
    right_half = arr[mid:]

    # --- CONQUISTA: ordena cada metade recursivamente ---
    counter[0] += 1  # conta a chamada/atribuição da ordenação da esquerda
    left_sorted = merge_sort(left_half, counter)

    counter[0] += 1  # conta a chamada/atribuição da ordenação da direita
    right_sorted = merge_sort(right_half, counter)

    # --- COMBINA: faz o merge das duas metades já ordenadas ---
    counter[0] += 1  # conta o return com chamada do merge
    return merge(left_sorted, right_sorted, counter)


def merge(left: list, right: list, counter: list) -> list:
    """
    Merge (combinação)
    Objetivo:
      - Receber duas listas ORDENADAS (left e right)
      - Produzir uma única lista ORDENADA, escolhendo sempre o menor elemento disponível
    Medida:
      - counter[0] soma 1 para cada linha/checagem executada (critério uniforme).
    """

    # Lista resultado
    counter[0] += 1  # conta a criação da lista de saída
    sorted_list = []

    # Ponteiros para percorrer left e right
    counter[0] += 1  # conta i = 0
    i = 0
    counter[0] += 1  # conta j = 0
    j = 0

    # Enquanto ainda houver elementos em ambas as listas:
    # - compara left[i] e right[j]
    # - adiciona o menor na saída
    counter[0] += 1  # conta a PRIMEIRA avaliação do while
    while i < len(left) and j < len(right):
        counter[0] += 1  # conta o IF (decisão de qual lado pegar)
        if left[i] <= right[j]:
            counter[0] += 1  # conta o append do elemento da esquerda
            sorted_list.append(left[i])
            counter[0] += 1  # conta o avanço do ponteiro i
            i += 1
        else:
            counter[0] += 1  # conta o append do elemento da direita
            sorted_list.append(right[j])
            counter[0] += 1  # conta o avanço do ponteiro j
            j += 1

        counter[0] += 1  # conta a PRÓXIMA avaliação do while (inclui a última que falha)

    # Quando uma das listas acaba, o resto da outra já está ordenado:
    # basta anexar tudo de uma vez
    counter[0] += 1  # conta o extend do restante da esquerda
    sorted_list.extend(left[i:])

    counter[0] += 1  # conta o extend do restante da direita
    sorted_list.extend(right[j:])

    counter[0] += 1  # conta o return da lista combinada
    return sorted_list