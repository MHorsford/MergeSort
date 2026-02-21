def merge_sort(arr: list, counter: list) -> list:
    """
        Ordena uma lista usando Merge Sort na versão recursiva (divide-and-conquer).

        Estratégia:
            1) Divide: separa a lista em duas metades.
            2) Conquista: ordena recursivamente cada metade.
            3) Combina: realiza o merge das duas metades já ordenadas.

        Métrica instrumentada:
            - "counter" deve ser uma lista com um único inteiro ("counter[0]").
            - "counter[0]" é incrementado ao longo da execução para contabilizar
            "linhas/checagens" conforme o critério adotado no experimento (proxy
            de custo operacional; não representa tempo de CPU).

        Parâmetros:
 
            arr : list
                Lista de valores comparáveis (suporta operações <=).
            counter : list
                Estrutura mutável para acumular a contagem (esperado: [0]).

        Retorna:
 
            list
                Nova lista ordenada em ordem não decrescente (crescente).
    """

    # Caso base - lista de tamanho 0 ou 1 já está ordenada
    counter[0] += 1  # conta a execução do if (checagem do caso base)
    if len(arr) <= 1:
        counter[0] += 1  # conta o return do caso base
        return arr

    # Divide - calcula o meio e cria as duas metades
    counter[0] += 1  # conta a atribuição do meio
    mid = len(arr) // 2

    counter[0] += 1  # conta a criação (fatia) da metade esquerda
    left_half = arr[:mid]

    counter[0] += 1  # conta a criação (fatia) da metade direita
    right_half = arr[mid:]

    # Conquista - ordena cada metade recursivamente
    counter[0] += 1  # conta a chamada - ligada da ordenação da esquerda
    left_sorted = merge_sort(left_half, counter)

    counter[0] += 1  # conta a chamada - ligada da ordenação da direita
    right_sorted = merge_sort(right_half, counter)

    # Combina - faz o merge das duas metades já ordenadas
    counter[0] += 1  # conta o return com chamada do merge
    return merge(left_sorted, right_sorted, counter)


def merge(left: list, right: list, counter: list) -> list:

    """
        Combina (merge) duas listas previamente ordenadas em uma única lista ordenada.

        Pré-condição:
        
            - "left" e "right" devem estar ordenadas em ordem não decrescente.

        Comportamento:
        
            Percorre simultaneamente "left" e "right" com ponteiros (i, j),
            comparando os elementos atuais e movendo o menor para a lista de saída.
            Ao final, anexa o restante da lista que ainda não foi consumida.

        Métrica instrumentada:
            - Incrementa "counter[0]" em checagens de laço, decisões (if/else),
            e operações centrais (append/extend), conforme o critério do experimento.

        Parâmetros:
        
            left : list
                Lista ordenada (crescente).
            right : list
                Lista ordenada (crescente).
            counter : list
                Estrutura mutável para acumular a contagem (esperado: [0]).

        Retorna:
        
            list
                Lista resultante ordenada contendo todos os elementos de "left" e "right".
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
    #   - compara left[i] e right[j]
    #   - adiciona o menor na saída
    counter[0] += 1  # conta a primeira avaliação do while
    while i < len(left) and j < len(right):
        counter[0] += 1  # conta o if (decisão de qual lado irá pegar)

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

        counter[0] += 1  # conta a prócima avaliação do while (inclui a última que falha)

    # Quando uma das listas acaba, o resto da outra já está ordenado:
    # basta anexar tudo de uma vez
    counter[0] += 1  # conta o extend do restante da esquerda
    sorted_list.extend(left[i:])

    counter[0] += 1  # conta o extend do restante da direita
    sorted_list.extend(right[j:])

    counter[0] += 1  # conta o return da lista combinada
    return sorted_list