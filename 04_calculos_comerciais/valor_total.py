"""
Cálculos de Valor Total

Funções para calcular totais de compras baseado em
preço unitário e quantidade.
"""


def calcular_valor_total(valor_unitario, quantidade):
    """
    Calcula o valor total de uma compra.
    
    Args:
        valor_unitario (float): Preço de uma unidade
        quantidade (int): Número de unidades
        
    Returns:
        float: Valor total da compra
        
    Exemplo:
        >>> calcular_valor_total(25.50, 3)
        76.5
        >>> calcular_valor_total(10.00, 5)
        50.0
    """
    return valor_unitario * quantidade


def calcular_valor_total_com_desconto(valor_unitario, quantidade, percentual_desconto=0):
    """
    Calcula o valor total com desconto aplicado.
    
    Args:
        valor_unitario (float): Preço de uma unidade
        quantidade (int): Número de unidades
        percentual_desconto (float): Percentual de desconto (0-100). Padrão: 0
        
    Returns:
        dict: Dicionário com subtotal, desconto e total final
        
    Exemplo:
        >>> calcular_valor_total_com_desconto(100, 2, 10)
        {'subtotal': 200, 'desconto': 20.0, 'total': 180.0}
    """
    subtotal = valor_unitario * quantidade
    valor_desconto = (subtotal * percentual_desconto) / 100
    total = subtotal - valor_desconto
    
    return {
        'subtotal': subtotal,
        'desconto': valor_desconto,
        'total': total,
    }


def processar_compra(valor_unitario, quantidade):
    """
    Processa uma compra e retorna informações formatadas.
    
    Args:
        valor_unitario (float): Preço unitário
        quantidade (int): Quantidade de produtos
        
    Returns:
        dict: Informações da compra
    """
    valor_total = calcular_valor_total(valor_unitario, quantidade)
    
    return {
        'valor_unitario': valor_unitario,
        'quantidade': quantidade,
        'valor_total': valor_total,
        'formatado': f"R$ {valor_total:.2f}"
    }
