import random as rd

class ListGerator:

    def __init__(self):
        pass

    def ordered(self, size: int) -> list:
        """
            - Gera uma lista ordenada
        """
        return sorted([rd.randint(0, size) for _ in range(size)])

    def disordered(self, size: int) -> list:
        """
            - gera uma lista desordenada
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
            - Gera uma lista em ordem decrescente 
        """
        return sorted([rd.randint(0, size) for _ in range(size)], reverse=True)
        
                

    def with_repetition(self, size: int) -> list:
        """
            - Gera uma lista com repetição.
            - Garantimos que haja no minimo 1 elemento repetido ao definir que o 
            intervalo dos elementos vai de 0 ao (tamanho da lista - 1)
            - Não gera lista vazia, sempre será um range de 1.
        """
        list_ = rd.choices(range(size - 1 if size > 1 else 1), k=size) 

        return list_
    
    def mixed_signs(self, size: int) -> list:
        """
            - Gera uma lista com números positivos e negativos
        """
        return [rd.randint(-size, size) for _ in range(size)]
    
    def all_equal(self, size: int, value: int = 100) -> list:
        """
            Gera uma lista onde todos os elementos são iguais 
        """
        return [value] * size
    
    def empty(self) -> list:
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
