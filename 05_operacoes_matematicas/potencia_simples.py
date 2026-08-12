"""
Cálculo de Potências Simples

Funções para calcular potências e quadrados de números.
Utiliza a biblioteca math para operações precisas.
"""

import math


def calcular_quadrado(numero):
    """
    Calcula o quadrado de um número (número²).
    
    Args:
        numero (int ou float): Número para calcular o quadrado
        
    Returns:
        int ou float: O quadrado do número
        
    Exemplo:
        >>> calcular_quadrado(5)
        25
        >>> calcular_quadrado(3.5)
        12.25
    """
    return int(math.pow(numero, 2))


def calcular_potencia(base, expoente):
    """
    Calcula a potência de um número (base^expoente).
    
    Args:
        base (int ou float): A base da potência
        expoente (int ou float): O expoente
        
    Returns:
        int: O resultado da potência (convertido para int)
        
    Exemplo:
        >>> calcular_potencia(2, 3)
        8
        >>> calcular_potencia(5, 2)
        25
    """
    return int(math.pow(base, expoente))


def calcular_potencia_com_validacao(base, expoente):
    """
    Calcula a potência com validação de entrada.
    
    Args:
        base: A base da potência
        expoente: O expoente
        
    Returns:
        float: O resultado da potência
        
    Raises:
        ValueError: Se base ou expoente não forem números válidos
    """
    try:
        base = float(base)
        expoente = float(expoente)
        return math.pow(base, expoente)
    except (ValueError, TypeError):
        raise ValueError(f"Base ({base}) e expoente ({expoente}) devem ser números.")
