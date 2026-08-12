"""
Cálculo de Potências Fracionárias

Funções para calcular potências com expoentes fracionários.
Suporta entrada em formato de fração (ex: "1/2" para raiz quadrada).
"""

import math


def calcular_potencia_fracionaria(base, expoente_str):
    """
    Calcula a potência de um número com expoente fracionário.
    
    Aceita expoentes em formato string:
    - Decimal: "0.5", "2.5"
    - Fração: "1/2", "3/4"
    - Inteiro: "2", "3"
    
    Args:
        base (int ou float): A base da potência
        expoente_str (str): O expoente em formato string
        
    Returns:
        int: O resultado da potência (convertido para int)
        
    Raises:
        ValueError: Se o formato do expoente for inválido
        
    Exemplo:
        >>> calcular_potencia_fracionaria(4, "0.5")  # Raiz quadrada
        2
        >>> calcular_potencia_fracionaria(8, "1/3")  # Raiz cúbica
        2
        >>> calcular_potencia_fracionaria(16, "1/4")  # Raiz quarta
        2
    """
    try:
        # Verifica se é uma fração
        if '/' in str(expoente_str):
            numerador, denominador = map(float, str(expoente_str).split('/'))
            if denominador == 0:
                raise ValueError("Denominador não pode ser zero")
            expoente = numerador / denominador
        else:
            # Se não é fração, trata como número decimal
            expoente = float(expoente_str)
        
        resultado = math.pow(base, expoente)
        return int(resultado)
    
    except ValueError as e:
        raise ValueError(f"Erro ao calcular potência: {e}")


def calcular_raiz_quadrada(numero):
    """
    Calcula a raiz quadrada de um número.
    
    Args:
        numero (int ou float): Número para calcular a raiz
        
    Returns:
        float: A raiz quadrada do número
        
    Exemplo:
        >>> calcular_raiz_quadrada(16)
        4.0
        >>> calcular_raiz_quadrada(2)
        1.414...
    """
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de números negativos")
    return math.sqrt(numero)


def calcular_raiz_n(numero, n):
    """
    Calcula a raiz n-ésima de um número.
    
    A raiz n-ésima é equivalente a elevar o número à potência 1/n.
    
    Args:
        numero (int ou float): Número para calcular a raiz
        n (int): Qual raiz calcular (2=quadrada, 3=cúbica, etc)
        
    Returns:
        float: A raiz n-ésima do número
        
    Exemplo:
        >>> calcular_raiz_n(8, 3)  # Raiz cúbica de 8
        2.0
        >>> calcular_raiz_n(16, 4)  # Raiz quarta de 16
        2.0
    """
    if n == 0:
        raise ValueError("Não é possível calcular raiz com índice 0")
    if numero < 0 and n % 2 == 0:
        raise ValueError(f"Não é possível calcular raiz {n} de números negativos")
    
    return numero ** (1 / n)
