"""
Tipos de Variáveis

Funções para verificar e demonstrar tipos de variáveis.
"""


def verificar_tipo(valor):
    """
    Retorna o tipo de uma variável.
    
    Args:
        valor: Qualquer valor para verificação de tipo
        
    Returns:
        type: O tipo da variável
        
    Exemplo:
        >>> verificar_tipo(42)
        <class 'int'>
        >>> verificar_tipo("texto")
        <class 'str'>
        >>> verificar_tipo(3.14)
        <class 'float'>
    """
    return type(valor)


def demonstrar_tipos():
    """
    Demonstra diferentes tipos de variáveis e suas conversões.
    
    Mostra:
    - Declaração de números inteiros
    - Declaração de números float
    - Conversão explícita de tipos
    - Verificação de tipos com type()
    """
    # Declaração de inteiros
    numero = 3
    numero1 = int(3)
    
    # Declaração de floats
    numero2 = float(3)
    numero3 = 3.0
    
    print("=== Demonstração de Tipos ===\n")
    
    print("Números inteiros:")
    print(f"numero = {numero} (tipo: {type(numero)})")
    print(f"numero1 = int(3) = {numero1} (tipo: {type(numero1)})")
    
    print("\nNúmeros float:")
    print(f"numero2 = float(3) = {numero2} (tipo: {type(numero2)})")
    print(f"numero3 = 3.0 = {numero3} (tipo: {type(numero3)})")
    
    print("\n=== Conversão de String ===")
    texto = "2"
    texto1 = str(2)
    texto2 = float(2)  # Declaração explícita
    
    print(f"texto = '2' (tipo: {type(texto)})")
    print(f"texto1 = str(2) = '{texto1}' (tipo: {type(texto1)})")
    print(f"texto2 = float(2) = {texto2} (tipo: {type(texto2)})")
    
    print("\n=== Valores Impressos ===")
    print(texto)
    print(texto1)
    print(texto2)
