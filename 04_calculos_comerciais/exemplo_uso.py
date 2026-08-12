"""
Exemplo de Uso - Cálculos Comerciais

Demonstra cálculo de valor total em cenários comerciais.
"""

from valor_total import calcular_valor_total, calcular_valor_total_com_desconto, processar_compra


def exemplo_valor_total_simples():
    """Exemplo básico de cálculo de valor total."""
    print("=" * 50)
    print("EXEMPLO 1: Cálculo de Valor Total Simples")
    print("=" * 50 + "\n")
    
    valor_uni = 25.50
    quantidade = 3
    
    print(f"Valor unitário: R$ {valor_uni}")
    print(f"Quantidade: {quantidade} produtos\n")
    
    valor_total = calcular_valor_total(valor_uni, quantidade)
    print(f"O total da compra é: R$ {valor_total:.2f}\n")


def exemplo_compras_multiplas():
    """Exemplo com múltiplas compras."""
    print("=" * 50)
    print("EXEMPLO 2: Múltiplas Compras")
    print("=" * 50 + "\n")
    
    compras = [
        {"valor": 10.00, "quantidade": 5},
        {"valor": 25.50, "quantidade": 2},
        {"valor": 15.99, "quantidade": 3},
        {"valor": 100.00, "quantidade": 1},
    ]
    
    total_geral = 0
    
    for i, compra in enumerate(compras, 1):
        valor_unitario = compra["valor"]
        quantidade = compra["quantidade"]
        
        valor_total = calcular_valor_total(valor_unitario, quantidade)
        total_geral += valor_total
        
        print(f"Compra {i}:")
        print(f"  Valor unitário: R$ {valor_unitario}")
        print(f"  Quantidade: {quantidade}")
        print(f"  Subtotal: R$ {valor_total:.2f}\n")
    
    print(f"Total geral: R$ {total_geral:.2f}\n")


def exemplo_valor_total_com_desconto():
    """Exemplo de cálculo com desconto."""
    print("=" * 50)
    print("EXEMPLO 3: Cálculo com Desconto")
    print("=" * 50 + "\n")
    
    valor_unitario = 100.00
    quantidade = 2
    desconto = 10
    
    resultado = calcular_valor_total_com_desconto(valor_unitario, quantidade, desconto)
    
    print(f"Valor unitário: R$ {valor_unitario}")
    print(f"Quantidade: {quantidade}")
    print(f"Desconto: {desconto}%\n")
    
    print(f"Subtotal: R$ {resultado['subtotal']:.2f}")
    print(f"Desconto: R$ {resultado['desconto']:.2f}")
    print(f"Total final: R$ {resultado['total']:.2f}\n")


def exemplo_processar_compra():
    """Exemplo de processamento completo de compra."""
    print("=" * 50)
    print("EXEMPLO 4: Processamento Completo de Compra")
    print("=" * 50 + "\n")
    
    valor_uni = 19.90
    quantidade = 4
    
    compra = processar_compra(valor_uni, quantidade)
    
    print(f"Informe o valor unitário: R$ {compra['valor_unitario']}")
    print(f"Informe a quantidade de produtos: {compra['quantidade']}\n")
    
    print(f"O total da compra é: {compra['formatado']}")


if __name__ == "__main__":
    exemplo_valor_total_simples()
    print()
    exemplo_compras_multiplas()
    print()
    exemplo_valor_total_com_desconto()
    print()
    exemplo_processar_compra()
