"""
Utilitários Compartilhados

Funções e classes auxiliares usadas em múltiplos módulos.
"""


def formatar_moeda(valor, moeda="R$"):
    """
    Formata um valor como moeda.
    
    Args:
        valor (float): Valor a formatar
        moeda (str): Símbolo da moeda. Padrão: "R$"
        
    Returns:
        str: Valor formatado como moeda
        
    Exemplo:
        >>> formatar_moeda(19.99)
        'R$ 19.99'
        >>> formatar_moeda(1000.50, "USD")
        'USD 1000.50'
    """
    return f"{moeda} {valor:.2f}"


def formatar_numero(numero, casas_decimais=2):
    """
    Formata um número com número específico de casas decimais.
    
    Args:
        numero (float): Número a formatar
        casas_decimais (int): Quantidade de casas decimais. Padrão: 2
        
    Returns:
        str: Número formatado
        
    Exemplo:
        >>> formatar_numero(3.14159)
        '3.14'
        >>> formatar_numero(19.5, 3)
        '19.500'
    """
    formato = f"{{:.{casas_decimais}f}}"
    return formato.format(numero)


def validar_numero_positivo(valor, mensagem="Valor deve ser positivo"):
    """
    Valida se um número é positivo.
    
    Args:
        valor (int ou float): Número a validar
        mensagem (str): Mensagem de erro customizada
        
    Returns:
        bool: True se é positivo, False caso contrário
        
    Raises:
        ValueError: Se o valor não for positivo
    """
    if valor <= 0:
        raise ValueError(mensagem)
    return True


def validar_numero_inteiro(valor):
    """
    Valida se um valor é um número inteiro válido.
    
    Args:
        valor: Valor a validar
        
    Returns:
        int: Valor convertido para int
        
    Raises:
        ValueError: Se o valor não puder ser convertido para int
    """
    try:
        return int(valor)
    except (ValueError, TypeError):
        raise ValueError(f"'{valor}' não é um número inteiro válido")


class Calculadora:
    """
    Classe auxiliar para operações matemáticas.
    
    Exemplo:
        >>> calc = Calculadora()
        >>> calc.somar(5, 3)
        8
        >>> calc.multiplicar(4, 2)
        8
    """
    
    @staticmethod
    def somar(a, b):
        """Soma dois números."""
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        """Subtrai dois números."""
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        """Multiplica dois números."""
        return a * b
    
    @staticmethod
    def dividir(a, b):
        """Divide dois números."""
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    @staticmethod
    def potencia(base, expoente):
        """Calcula a potência."""
        return base ** expoente
