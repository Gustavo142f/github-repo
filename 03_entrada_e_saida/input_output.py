"""
Funções de Entrada e Saída

Funções para ler dados do usuário e exibir resultados formatados.
"""


def ler_nome():
    """
    Lê o nome do usuário.
    
    Returns:
        str: Nome digitado pelo usuário
        
    Exemplo:
        >>> nome = ler_nome()
        Digite o seu nome: João
        >>> print(nome)
        João
    """
    nome = input("Digite o seu nome: ")
    return nome


def exibir_nome(nome):
    """
    Exibe uma mensagem com o nome fornecido.
    
    Args:
        nome: Nome a ser exibido
    """
    print("O seu nome é: ", nome)


def ler_numero():
    """
    Lê um número inteiro do usuário.
    
    Returns:
        int: Número inteiro digitado
        
    Raises:
        ValueError: Se a entrada não for um número válido
        
    Exemplo:
        >>> numero = ler_numero()
        Digite um número: 5
        >>> print(numero * 2)
        10
    """
    try:
        numero = int(input("Digite um número: "))
        return numero
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")
        return None


def ler_inteiro_com_mensagem(mensagem):
    """
    Lê um número inteiro com mensagem personalizada.
    
    Args:
        mensagem: Mensagem a ser exibida para o usuário
        
    Returns:
        int: Número inteiro digitado
        
    Exemplo:
        >>> numero = ler_inteiro_com_mensagem("Informe um número inteiro: ")
    """
    try:
        numero = int(input(mensagem))
        return numero
    except ValueError:
        print(f"Erro: '{input}' não é um número inteiro válido.")
        return None


def ler_float():
    """
    Lê um número float (ponto flutuante) do usuário.
    
    Returns:
        float: Número float digitado
        
    Raises:
        ValueError: Se a entrada não for um número válido
        
    Exemplo:
        >>> valor = ler_float()
        Digite um valor: 19.99
        >>> print(valor)
        19.99
    """
    try:
        valor = float(input("Digite um valor: "))
        return valor
    except ValueError:
        print("Erro: Entrada inválida. Digite um número.")
        return None


def ler_float_com_mensagem(mensagem):
    """
    Lê um número float com mensagem personalizada.
    
    Args:
        mensagem: Mensagem a ser exibida
        
    Returns:
        float: Número float digitado
        
    Exemplo:
        >>> valor = ler_float_com_mensagem("Informe o valor unitário: ")
    """
    try:
        valor = float(input(mensagem))
        return valor
    except ValueError:
        print(f"Erro: Entrada inválida.")
        return None
