"""
Operações Aritméticas Básicas

Funções para realizar operações matemáticas simples.
"""


def duplicar_numero(numero):
    """
    Duplica um número multiplicando por 2.
    
    Args:
        numero: Número inteiro ou float
        
    Returns:
        Número multiplicado por 2
        
    Exemplo:
        >>> duplicar_numero(5)
        10
        >>> duplicar_numero(3.5)
        7.0
    """
    return numero * 2


def calcular_operacoes(a, b):
    """
    Realiza operações aritméticas básicas entre dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        dict: Dicionário com resultados das operações
        
    Exemplo:
        >>> calcular_operacoes(10, 3)
        {'soma': 13, 'subtracao': 7, 'multiplicacao': 30, 'divisao': 3.333...}
    """
    return {
        'soma': a + b,
        'subtracao': a - b,
        'multiplicacao': a * b,
        'divisao': a / b if b != 0 else None,
        'resto': a % b if b != 0 else None,
    }


def somar_com_inteiro(texto):
    """
    Soma 1 a um valor em string convertido para inteiro.
    
    Args:
        texto: String representando um número
        
    Returns:
        int: Resultado da soma
        
    Exemplo:
        >>> somar_com_inteiro("2")
        3
    """
    return 1 + int(texto)
