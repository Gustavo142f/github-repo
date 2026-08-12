"""
Conversão Básica de Tipos

Funções para converter entre tipos primitivos:
string, inteiro e ponto flutuante.
"""


def converter_para_inteiro(valor):
    """
    Converte um valor para inteiro.
    
    Args:
        valor: String, float ou int a ser convertido
        
    Returns:
        int: Valor convertido para inteiro
        
    Raises:
        ValueError: Se o valor não puder ser convertido
        
    Exemplo:
        >>> converter_para_inteiro("42")
        42
        >>> converter_para_inteiro(3.14)
        3
    """
    try:
        return int(valor)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Não foi possível converter '{valor}' para inteiro: {e}")


def converter_para_float(valor):
    """
    Converte um valor para ponto flutuante.
    
    Args:
        valor: String, int ou float a ser convertido
        
    Returns:
        float: Valor convertido para float
        
    Raises:
        ValueError: Se o valor não puder ser convertido
        
    Exemplo:
        >>> converter_para_float("3.14")
        3.14
        >>> converter_para_float(42)
        42.0
    """
    try:
        return float(valor)
    except (ValueError, TypeError) as e:
        raise ValueError(f"Não foi possível converter '{valor}' para float: {e}")


def converter_para_string(valor):
    """
    Converte um valor para string.
    
    Args:
        valor: Qualquer valor a ser convertido
        
    Returns:
        str: Valor convertido para string
        
    Exemplo:
        >>> converter_para_string(42)
        '42'
        >>> converter_para_string(3.14)
        '3.14'
    """
    return str(valor)
