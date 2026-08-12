"""
Exemplo de Uso - Tipos e Conversões

Demonstra conversões básicas e verificação de tipos.
"""

from conversao_basica import converter_para_inteiro, converter_para_float, converter_para_string
from tipos_variaveis import verificar_tipo, demonstrar_tipos


def exemplo_conversoes_simples():
    """Exemplo de conversões simples com tratamento de erros."""
    print("=" * 50)
    print("EXEMPLO 1: Conversões Simples")
    print("=" * 50 + "\n")
    
    # Conversão de string para inteiro
    valor_str = "42"
    valor_int = converter_para_inteiro(valor_str)
    print(f"String '{valor_str}' → Inteiro: {valor_int}")
    print(f"Tipo: {verificar_tipo(valor_int)}\n")
    
    # Conversão de float para inteiro
    valor_float = 3.14
    valor_int2 = converter_para_inteiro(valor_float)
    print(f"Float {valor_float} → Inteiro: {valor_int2}")
    print(f"Tipo: {verificar_tipo(valor_int2)}\n")
    
    # Conversão para float
    valor_float2 = converter_para_float("19.99")
    print(f"String '19.99' → Float: {valor_float2}")
    print(f"Tipo: {verificar_tipo(valor_float2)}\n")
    
    # Conversão para string
    valor_string = converter_para_string(100)
    print(f"Inteiro 100 → String: '{valor_string}'")
    print(f"Tipo: {verificar_tipo(valor_string)}\n")


def exemplo_operacoes_com_conversao():
    """Exemplo de operações aritméticas com conversão."""
    print("=" * 50)
    print("EXEMPLO 2: Operações com Conversão")
    print("=" * 50 + "\n")
    
    texto = "2"
    print(f"texto = '{texto}' (tipo: {verificar_tipo(texto)})")
    
    # Soma com conversão
    soma = 1 + converter_para_inteiro(texto)
    print(f"soma = 1 + int('{texto}') = {soma}\n")
    
    # Usando float
    texto2 = converter_para_float(2)
    soma2 = 1 + texto2
    print(f"texto2 = float(2) = {texto2}")
    print(f"soma = 1 + {texto2} = {soma2}\n")


def exemplo_verificacao_tipos():
    """Exemplo de verificação de tipos."""
    print("=" * 50)
    print("EXEMPLO 3: Verificação de Tipos")
    print("=" * 50 + "\n")
    
    valores = [
        42,
        3.14,
        "texto",
        True,
        [1, 2, 3],
        {"chave": "valor"}
    ]
    
    for valor in valores:
        tipo = verificar_tipo(valor)
        print(f"Valor: {valor:20} → Tipo: {tipo}")


if __name__ == "__main__":
    exemplo_conversoes_simples()
    print("\n")
    exemplo_operacoes_com_conversao()
    print("\n")
    exemplo_verificacao_tipos()
    print("\n")
    print("=" * 50)
    print("DEMONSTRAÇÃO COMPLETA DE TIPOS")
    print("=" * 50 + "\n")
    demonstrar_tipos()
