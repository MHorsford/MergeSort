from mergesort import merge
def merge_sort_bottom_up(arr: list, counter: list) -> list:
    """
    Merge Sort (iterativo / bottom-up)
    Ideia:
      - Em vez de dividir recursivamente, começa com "blocos" de tamanho 1 (já ordenados)
      - Vai dobrando o tamanho do bloco (width = 1, 2, 4, 8, ...)
      - Em cada passo, faz merge de pares de blocos adjacentes

    Medida:
      - counter[0] soma 1 para cada linha/checagem executada (critério uniforme).
    """

    # Caso trivial
    counter[0] += 1  # conta o IF
    if len(arr) <= 1:
        counter[0] += 1  # conta o return
        return arr

    # width representa o tamanho do bloco ordenado atual
    counter[0] += 1  # conta width = 1
    width = 1

    # Enquanto o bloco for menor que o tamanho da lista:
    counter[0] += 1  # conta a PRIMEIRA avaliação do while
    while width < len(arr):

        # Percorre a lista juntando pares de blocos de tamanho width:
        # [i : i+width] com [i+width : i+2*width]
        counter[0] += 1  # conta a entrada/inicialização do for
        for i in range(0, len(arr), 2 * width):
            counter[0] += 1  # conta a iteração do for (checagem passou)

            # Separa os dois blocos (metades)
            counter[0] += 1  # conta left_half = ...
            left_half = arr[i : i + width]

            counter[0] += 1  # conta right_half = ...
            right_half = arr[i + width : i + 2 * width]

            # Faz merge dos dois blocos ordenados
            counter[0] += 1  # conta merged = merge(...)
            merged = merge(left_half, right_half, counter)

            # Substitui o trecho original pelo trecho mesclado
            counter[0] += 1  # conta arr[...] = merged
            arr[i : i + 2 * width] = merged

        counter[0] += 1  # conta a checagem final do for (quando ele sai)

        # Dobra o tamanho do bloco para o próximo “nível”
        counter[0] += 1  # conta width *= 2
        width *= 2

        counter[0] += 1  # conta a PRÓXIMA avaliação do while (inclui a última que falha)

    counter[0] += 1  # conta o return final
    return arr