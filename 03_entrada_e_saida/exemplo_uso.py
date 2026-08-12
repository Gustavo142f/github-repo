"""
Exemplo de Uso - Entrada e Saída

Demonstra leitura de dados do usuário e formatação de saída.

NOTA: Este script foi adaptado para fins de demonstração.
Em um uso real, descomente as linhas com input().
"""

from input_output import (
    ler_nome, exibir_nome, ler_numero, 
    ler_inteiro_com_mensagem, ler_float, ler_float_com_mensagem
)


def exemplo_ler_nome():
    """Exemplo de leitura de nome."""
    print("=" * 50)
    print("EXEMPLO 1: Leitura de Nome")
    print("=" * 50 + "\n")
    
    # Em um uso real, descomente a linha abaixo:
    # nome = ler_nome()
    
    # Para demonstração:
    nome = "João Silva"
    print(f"Digite o seu nome: {nome}")
    
    exibir_nome(nome)
    print()


def exemplo_ler_numero():
    """Exemplo de leitura de número."""
    print("=" * 50)
    print("EXEMPLO 2: Leitura de Número Inteiro")
    print("=" * 50 + "\n")
    
    # Em um uso real, descomente a linha abaixo:
    # a = ler_numero()
    
    # Para demonstração:
    a = 5
    print(f"Digite um número: {a}")
    
    b = a * 2
    print(f"Número × 2 = {b}\n")


def exemplo_ler_float():
    """Exemplo de leitura de float (valor em reais)."""
    print("=" * 50)
    print("EXEMPLO 3: Leitura de Valor Float")
    print("=" * 50 + "\n")
    
    # Em um uso real, descomente as linhas abaixo:
    # valor_uni = ler_float_com_mensagem("Informe o valor unitário: ")
    # quantidade = ler_inteiro_com_mensagem("Informe a quantidade de produtos: ")
    
    # Para demonstração:
    valor_uni = 25.50
    quantidade = 3
    
    print(f"Informe o valor unitário: {valor_uni}")
    print(f"Informe a quantidade de produtos: {quantidade}")
    
    valor_total = valor_uni * quantidade
    print(f"O total da compra é: {valor_total}\n")


def exemplo_calcular_valor_total():
    """Exemplo de cálculo de valor total."""
    print("=" * 50)
    print("EXEMPLO 4: Cálculo de Valor Total (Repetição)")
    print("=" * 50 + "\n")
    
    # Em um uso real, descomente:
    # valor_uni = ler_float_com_mensagem("Informe o valor unitário: ")
    # quantidade = ler_inteiro_com_mensagem("Informe a quantidade de produtos: ")
    
    # Para demonstração:
    valor_uni = 15.99
    quantidade = 2
    
    print(f"Informe o valor unitário: {valor_uni}")
    print(f"Informe a quantidade de produtos: {quantidade}\n")
    
    # Primeira forma
    valor_total = valor_uni * quantidade
    print(f"Cálculo 1 - O total da compra é: {valor_total}\n")
    
    # Repetindo o cálculo (sem re-ler os dados)
    valor_total = valor_uni * quantidade
    print(f"Cálculo 2 - O total da compra é: {valor_total}")


if __name__ == "__main__":
    exemplo_ler_nome()
    exemplo_ler_numero()
    exemplo_ler_float()
    exemplo_calcular_valor_total()
    
    print("\n" + "=" * 50)
    print("NOTA: Para usar com entrada real do usuário,")
    print("descomente as linhas com input() no código.")
    print("=" * 50)
