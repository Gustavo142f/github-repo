"""
Exemplo de Uso - Operações Matemáticas Avançadas

Demonstra cálculo de potências simples e fracionárias.
"""

from potencia_simples import calcular_quadrado, calcular_potencia, calcular_potencia_com_validacao
from potencia_fracionaria import calcular_potencia_fracionaria, calcular_raiz_quadrada, calcular_raiz_n


def exemplo_quadrado():
    """Exemplo de cálculo de quadrado."""
    print("=" * 50)
    print("EXEMPLO 1: Cálculo de Quadrado")
    print("=" * 50 + "\n")
    
    numero = 5
    quadrado = calcular_quadrado(numero)
    
    print(f"Informe um número inteiro: {numero}")
    print(f"O quadrado do número informado é: {quadrado}\n")
    
    # Mais exemplos
    numeros = [1, 2, 3, 4, 5, 10]
    print("Mais exemplos:")
    for n in numeros:
        resultado = calcular_quadrado(n)
        print(f"{n}² = {resultado}")


def exemplo_potencia_simples():
    """Exemplo de cálculo de potência simples."""
    print("\n" + "=" * 50)
    print("EXEMPLO 2: Cálculo de Potência Simples")
    print("=" * 50 + "\n")
    
    base = 2
    expoente = 3
    
    resultado = calcular_potencia(base, expoente)
    print(f"Base: {base}")
    print(f"Expoente: {expoente}")
    print(f"Resultado: {base}^{expoente} = {resultado}\n")
    
    # Mais exemplos
    exemplos = [(2, 2), (2, 3), (3, 3), (5, 2), (10, 3)]
    print("Mais exemplos:")
    for b, e in exemplos:
        resultado = calcular_potencia(b, e)
        print(f"{b}^{e} = {resultado}")


def exemplo_potencia_fracionaria():
    """Exemplo de cálculo de potência fracionária."""
    print("\n" + "=" * 50)
    print("EXEMPLO 3: Cálculo de Potência Fracionária")
    print("=" * 50 + "\n")
    
    numero1 = 16
    expoente_str = "1/2"  # Raiz quadrada
    
    resultado = calcular_potencia_fracionaria(numero1, expoente_str)
    
    print(f"Informe um número inteiro: {numero1}")
    print(f"Informe o expoente: {expoente_str}")
    print(f"A potência do número informado é: {resultado}\n")
    
    # Mais exemplos de raízes
    print("Exemplos de raízes:")
    print(f"√4 (4^(1/2)) = {calcular_potencia_fracionaria(4, '1/2')}")
    print(f"∛8 (8^(1/3)) = {calcular_potencia_fracionaria(8, '1/3')}")
    print(f"⁴√16 (16^(1/4)) = {calcular_potencia_fracionaria(16, '1/4')}")
    print(f"2^(3/2) = {calcular_potencia_fracionaria(2, '3/2')}")


def exemplo_raiz_quadrada():
    """Exemplo de cálculo de raiz quadrada."""
    print("\n" + "=" * 50)
    print("EXEMPLO 4: Cálculo de Raiz Quadrada")
    print("=" * 50 + "\n")
    
    numeros = [4, 9, 16, 25, 2, 10]
    
    print("Raízes quadradas:")
    for n in numeros:
        resultado = calcular_raiz_quadrada(n)
        print(f"√{n} = {resultado:.4f}")


def exemplo_raiz_n():
    """Exemplo de cálculo de raiz n-ésima."""
    print("\n" + "=" * 50)
    print("EXEMPLO 5: Cálculo de Raiz n-ésima")
    print("=" * 50 + "\n")
    
    print("Raízes cúbicas (∛):")
    print(f"∛8 = {calcular_raiz_n(8, 3):.4f}")
    print(f"∛27 = {calcular_raiz_n(27, 3):.4f}")
    print(f"∛64 = {calcular_raiz_n(64, 3):.4f}\n")
    
    print("Raízes quartas (⁴√):")
    print(f"⁴√16 = {calcular_raiz_n(16, 4):.4f}")
    print(f"⁴√81 = {calcular_raiz_n(81, 4):.4f}\n")
    
    print("Raízes quintas (⁵√):")
    print(f"⁵√32 = {calcular_raiz_n(32, 5):.4f}")
    print(f"⁵√243 = {calcular_raiz_n(243, 5):.4f}")


if __name__ == "__main__":
    exemplo_quadrado()
    exemplo_potencia_simples()
    exemplo_potencia_fracionaria()
    exemplo_raiz_quadrada()
    exemplo_raiz_n()
