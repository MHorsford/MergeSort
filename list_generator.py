import random as rd

class ListGerator:
    """
        Gerador de listas para os cenários de teste do experimento.

        Observações:
            - O gerador fixa a semente do RNG em "seed(1)" no construtor, tornando a
            sequência de listas reprodutível entre execuções.
            - Os métodos retornam novas listas (não modificam listas externas).
    """

    def __init__(self):
        """
            Inicializa o gerador e fixa a semente pseudo-aleatória para reprodutibilidade.
        """
        rd.seed(1)

    def ordered(self, size: int) -> list:
        """
            Gera uma lista ordenada em ordem crescente.

            Parâmetros:
            
                size : int
                    Tamanho da lista.

            Retorna:
        
                list
                    Lista com "size" inteiros no intervalo [0, size], ordenada crescentemente.
        """
        return sorted([rd.randint(0, size) for _ in range(size)])

    def disordered(self, size: int) -> list:
        """
            Gera uma lista desordenada (pseudo-aleatória), evitando casos degenerados.

            Estratégia:
                - Gera uma lista com "size" inteiros no intervalo [0, size].
                - Se por acaso a lista gerar todos os elementos iguais (ex.: [2,2,2]) e
                "size > 1", altera o último elemento para garantir pelo menos 2 valores distintos.
                - Se por acaso a lista gerar já ordenada, embaralha até deixar de estar ordenada.

            Parâmetros:
            
                size : int
                    Tamanho da lista.

            Retorna:
            
                list
                    Lista pseudo-aleatória que, com as correções acima, tende a não estar ordenada.
        """
        list_ = [rd.randint(0, size) for _ in range(size)]
        
        repeating = len(set(list_))
        if repeating == 1 and 1 < size: # o Set terá tamanho 1 se os elementos forem todos iguais, ex: [2, 2, 2]
            list_[-1] = 0 if list_[-1] > 0 else -1 # Troca o ultimo elemento para 0 ou -1 garantindo um valor menor no fim
            return list_
            
        if list_ == sorted(list_): # Varifica se a lista gerada seria igual uma lista ordenada
            while list_ == sorted(list_): # O laço para assim que a lista não for mais igual
                rd.shuffle(list_)
            return list_
        return list_
    
    def reverse_ordered(self, size: int) -> list:
        """
            Gera uma lista em ordem decrescente (reversa).

            Parâmetros:
                size : int
                    Tamanho da lista.

            Retorna:
            
                list
                    Lista com "size" inteiros no intervalo [0, size], ordenada decrescentemente.
        """
        return sorted([rd.randint(0, size) for _ in range(size)], reverse=True)
        
                

    def with_repetition(self, size: int) -> list:
        """
            Gera uma lista com repetição garantida (sempre que "size > 1").

            Estratégia:
                - Usa rd.choices em um intervalo menor que o tamanho, forçando colisões
                (valores repetidos) quando "size > 1".
                - Para "size <= 1", usa um intervalo mínimo para evitar range vazio.

            Parâmetros:
            
                size : int
                    Tamanho da lista.

            Retorna:

                list
                    Lista de tamanho `size` contendo valores repetidos (quando possível).
        """
        list_ = rd.choices(range(size - 1 if size > 1 else 1), k=size) 

        return list_
    
    def mixed_signs(self, size: int) -> list:
        """
            Gera uma lista com valores positivos e negativos.

            Parâmetros:
            
                size : int
                    Tamanho da lista.

            Retorna:
            
                list
                    Lista com "size" inteiros no intervalo [-size, size].
        """
        return [rd.randint(-size, size) for _ in range(size)]
    
    def all_equal(self, size: int, value: int = 100) -> list:
        """
            Gera uma lista onde todos os elementos são iguais.

            Parâmetros:
            
                size : int
                    Tamanho da lista.
                value : int, default=100
                    Valor repetido em todas as posições.

            Retorna:
            
                list
                    Lista de tamanho `size` onde todos os elementos são `value`.
        """
        return [value] * size
    
    def empty(self) -> list:
        """
            Gera uma lista vazia.

            Retorna:
            
                list
                    Lista vazia [].
        """
        return []

if __name__ == '__main__':
    lg = ListGerator()
    print(lg.ordered(10))
    print(lg.disordered(10))
    print(lg.reverse_ordered(10))
    print(lg.with_repetition(10))
    print(lg.mixed_signs(10))
    print(lg.all_equal(10))
    print(lg.empty())
