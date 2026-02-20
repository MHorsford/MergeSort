import matplotlib.pyplot as plt

from list_generator import ListGerator
from mergesort import merge_sort
from merge_sort_bottom_up import merge_sort_bottom_up


def run_and_count(alg_fn, base_list):
    """
    Roda um algoritmo de ordenação instrumentado e retorna:
      - resultado ordenado
      - contador de "linhas/checagens executadas"
    """
    counter = [0]
    data = base_list[:]  # copia para não alterar a base
    result = alg_fn(data, counter)
    return result, counter[0]


def benchmark_case(case_name, gen_fn, sizes, repeats, print_each_run=True):
    """
    Para um tipo de entrada (ex.: desordenada), executa a bateria e:
      - imprime no terminal as contagens
      - devolve médias por N (para plotar)
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
    plt.figure()
    plt.plot(sizes, rec_means, marker="o", label="Merge Sort recursivo")
    plt.plot(sizes, it_means, marker="o", label="Merge Sort bottom-up")
    plt.xlabel("Tamanho da entrada (N)")
    plt.ylabel("Linhas/checagens executadas (média)")
    plt.title(title)
    plt.grid(True)
    plt.legend()


def main():
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