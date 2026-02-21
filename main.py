import matplotlib.pyplot as plt

from list_generator import ListGerator
from mergesort import merge_sort
from merge_sort_bottom_up import merge_sort_bottom_up


def run_and_count(alg_fn, base_list):
    """
        Executa um algoritmo de ordenação *instrumentado* e devolve:
            (1) a lista ordenada (resultado do algoritmo)
            (2) a contagem total de "linhas/checagens" acumulada no contador

        Parâmetros:

            alg_fn : callable
                Função do algoritmo de ordenação. Espera-se que tenha a assinatura:
                    alg_fn(lista, counter) -> lista_ordenada
                onde `counter` é uma lista com um inteiro (ex.: [0]) usada para somar
                incrementos durante a execução.
            base_list : list
                Lista base de entrada. Ela NÃO é modificada diretamente; o método cria
                uma cópia antes de chamar o algoritmo.

        Retorno:
        
            tuple[list, int]
                result : list
                    Lista ordenada retornada por "alg_fn".
                count : int
                    Valor final do contador (quantidade de linhas/checagens executadas).

        Observações:

            - A cópia "data = base_list[:]" evita que uma execução altere a entrada
            que será usada por outro algoritmo na mesma repetição.
            - A métrica medida NÃO é tempo de CPU; é uma contagem instrumentada no código.
    """
    counter = [0]
    data = base_list[:]  # copia para não alterar a base
    result = alg_fn(data, counter)
    return result, counter[0]


def benchmark_case(case_name, gen_fn, sizes, repeats, print_each_run=True):
    """
        Executa a bateria de testes para um determinado cenário de entrada
        (ex.: "Desordenada", "Ordenada", etc.) e retorna as médias das contagens
        para cada tamanho N, comparando:
            - Merge Sort recursivo
            - Merge Sort bottom-up (iterativo)

        Parâmetros:
            
            case_name : str
                Nome do caso/cenário (usado para impressão e título de gráfico).
            gen_fn : callable
                Função geradora de listas do cenário. Deve aceitar um inteiro N e
                retornar uma lista de tamanho N:
                    gen_fn(N) -> list
            sizes : list[int]
                Tamanhos de entrada testados (ex.: [10, 100, 1000, ...]).
            repeats : int
                Número de repetições por tamanho N (ex.: 5).
            print_each_run : bool, default=True
                Se True, imprime a contagem de cada repetição individualmente.
                Se False, imprime apenas o resumo (média, min e max) por N.

        Retorno:
        
            tuple[list[float], list[float]]
                rec_means : lista de médias do Merge Sort recursivo para cada N.
                it_means  : lista de médias do Merge Sort bottom-up para cada N.

        Procedimento:

            Para cada N em "sizes":
                1) executa "repeats" vezes:
                    - gera lista base com "gen_fn(N)"
                    - roda merge_sort (recursivo) e merge_sort_bottom_up
                    - valida as saídas comparando com "sorted(base)"
                    - acumula contagens rec_counts e it_counts
                2) calcula média, mínimo e máximo
                3) armazena as médias para posterior plotagem
    """
    rec_means = []
    it_means = []

    print("\n" + "=" * 80)
    print(f"CASO: {case_name}")
    print("=" * 80)

    for n in sizes:
        rec_counts = []
        it_counts = []

        print(f"\nN = {n} | repetições = {repeats}")
        print("-" * 80)

        for r in range(1, repeats + 1):
            base = gen_fn(n)

            # Recursivo
            rec_sorted, rec_c = run_and_count(merge_sort, base)
            # Bottom-up
            it_sorted, it_c = run_and_count(merge_sort_bottom_up, base)

            # validação (garante que os dois ordenam certo)
            expected = sorted(base)
            assert rec_sorted == expected
            assert it_sorted == expected

            rec_counts.append(rec_c)
            it_counts.append(it_c)

            if print_each_run:
                print(f"rep {r:02d} | recursivo: {rec_c:8d} linhas | bottom-up: {it_c:8d} linhas")

        rec_avg = sum(rec_counts) / repeats
        it_avg = sum(it_counts) / repeats

        rec_means.append(rec_avg)
        it_means.append(it_avg)

        print("-" * 80)
        print(f"MÉDIA   | recursivo: {rec_avg:8.1f} linhas | bottom-up: {it_avg:8.1f} linhas")
        print(f"MIN/MAX | recursivo: {min(rec_counts):8d}/{max(rec_counts):8d} | bottom-up: {min(it_counts):8d}/{max(it_counts):8d}")

    return rec_means, it_means


def plot_case(sizes, rec_means, it_means, title):
    """
        Gera um gráfico (matplotlib) comparando as médias de linhas/checagens
        para os dois algoritmos em função do tamanho de entrada N.

        Parâmetros:
            sizes : list[int]
                Tamanhos N usados no eixo X.
            rec_means : list[float]
                Médias do Merge Sort recursivo para cada N.
            it_means : list[float]
                Médias do Merge Sort bottom-up para cada N.
            title : str
                Título do gráfico (inclui o nome do cenário).

        Saída:

            Abre uma figura com:
                - linha do recursivo
                - linha do bottom-up
                - grade, legenda e rótulos de eixos
    """
    plt.figure()
    plt.plot(sizes, rec_means, marker="o", label="Merge Sort recursivo")
    plt.plot(sizes, it_means, marker="o", label="Merge Sort bottom-up")
    plt.xlabel("Tamanho da entrada (N)")
    plt.ylabel("Linhas/checagens executadas (média)")
    plt.title(title)
    plt.grid(True)
    plt.legend()


def main():
    """
        Função principal do experimento.

        Etapas:
            1) instancia o gerador de listas (ListGerator)
            2) define tamanhos "sizes" e número de repetições "repeats"
            3) define os cenários (nome, função geradora)
            4) para cada cenário:
                - executa benchmark_case -> obtém médias por N
                - plota o gráfico do cenário
            5) exibe todos os gráficos com plt.show()
    """
    lg = ListGerator()

    # tamanhos e repetições (ajuste conforme seu PC/tempo)
    sizes = [10, 100, 1000, 10000, 50000, 100000]
    repeats = 5

    # casos de teste do seu gerador
    cases = [
        ("Desordenada", lg.disordered),
        ("Ordenada", lg.ordered),
        ("Reversa", lg.reverse_ordered),
        ("Com repetição", lg.with_repetition),
        ("Sinais mistos", lg.mixed_signs),
    ]

    for case_name, gen_fn in cases:
        rec_means, it_means = benchmark_case(
            case_name=case_name,
            gen_fn=gen_fn,
            sizes=sizes,
            repeats=repeats,
            print_each_run=True,   # deixe True para ver a contagem “exata” por execução
        )
        plot_case(sizes, rec_means, it_means, f"Desempenho por linhas - {case_name}")

    plt.show()


if __name__ == "__main__":
    main()