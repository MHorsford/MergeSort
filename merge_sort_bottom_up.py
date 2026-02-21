from mergesort import merge
def merge_sort_bottom_up(arr: list, counter: list) -> list:
    """
        Ordena uma lista usando Merge Sort na versão iterativa bottom-up.
        Reutiliza a função merge() do módulo mergesort.

        Ideia:
            - Em vez de dividir recursivamente, o algoritmo mescla blocos de tamanho 1,
            depois 2, 4, 8, ... até cobrir toda a lista.
            - A variável "width" representa o tamanho atual dos blocos a serem mesclados.

        Fluxo:
            1) Define "width = 1".
            2) Para cada par de blocos adjacentes (left..mid) e (mid..right),
            realiza o merge no vetor auxiliar.
            3) Copia o resultado de volta para "arr".
            4) Dobra "width" e repete até "width >= n".

        Métrica instrumentada:
            - "counter" deve ser uma lista com um único inteiro ("counter[0]").
            - "counter[0]" é incrementado em checagens/decisões/operações centrais
            conforme o critério do experimento (proxy de custo operacional, não tempo).

        Parâmetros:
        
            arr : list
                Lista de valores comparáveis (suporta operações <=).
            counter : list
                Estrutura mutável para acumular a contagem (esperado: [0]).

        Retorna:
        
            list
                A própria lista "arr" ordenada em ordem não decrescente (crescente).
    """
    # Caso trivial
    counter[0] += 1  # conta o if
    if len(arr) <= 1:
        counter[0] += 1  # conta o return
        return arr
    
    # width representa o tamanho do bloco ordenado atual
    counter[0] += 1  # conta width = 1
    width = 1

    # Enquanto o bloco for menor que o tamanho da lista:
    counter[0] += 1  # conta a primeira avaliação do while

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
        counter[0] += 1  # conta a proxima avaliação do while (inclui a última que falha)

    counter[0] += 1  # conta o return final
    return arr