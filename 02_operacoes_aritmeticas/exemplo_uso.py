"""
Exemplo de Uso - Operações Aritméticas

Demonstra operações matemáticas básicas.
"""

from operacoes_basicas import duplicar_numero, calcular_operacoes, somar_com_inteiro


def exemplo_duplicar():
    """Exemplo de duplicação de números."""
    print("=" * 50)
    print("EXEMPLO 1: Duplicação de Números")
    print("=" * 50 + "\n")
    
    numeros = [1, 5, 10, 3.5, 7.2]
    
    for num in numeros:
        resultado = duplicar_numero(num)
        print(f"{num} × 2 = {resultado}")


def exemplo_operacoes_basicas():
    """Exemplo de operações aritméticas."""
    print("\n" + "=" * 50)
    print("EXEMPLO 2: Operações Aritméticas Básicas")
    print("=" * 50 + "\n")
    
    pares = [(10, 3), (20, 4), (15, 2)]
    
    for a, b in pares:
        resultado = calcular_operacoes(a, b)
        print(f"Operações entre {a} e {b}:")
        for operacao, valor in resultado.items():
            print(f"  {operacao}: {valor}")
        print()


def exemplo_soma_string():
    """Exemplo de soma com conversão de string."""
    print("=" * 50)
    print("EXEMPLO 3: Soma com Conversão de String")
    print("=" * 50 + "\n")
    
    texto = "2"
    textoTransformado = int(texto)
    
    print(f"texto = '{texto}' (tipo string)")
    print(f"textoTransformado = int('{texto}') = {textoTransformado}")
    
    soma = somar_com_inteiro(texto)
    print(f"soma = 1 + int('{texto}') = {soma}\n")
    
    # Também usando a variável transformada
    soma2 = 1 + textoTransformado
    print(f"soma = 1 + {textoTransformado} = {soma2}")


if __name__ == "__main__":
    exemplo_duplicar()
    exemplo_operacoes_basicas()
    exemplo_soma_string()
