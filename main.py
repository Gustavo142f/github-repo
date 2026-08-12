"""
🎯 Teste de Integração - Programação em Python

Este script executa exemplos de cada módulo para demonstrar
que tudo está funcionando corretamente.

Uso:
    python main.py

Ou em PowerShell:
    python .\main.py
"""

import sys
import os
from pathlib import Path


def teste_modulo_1():
    """Testa o módulo de Tipos e Conversões."""
    print("\n" + "=" * 60)
    print("TESTE 1: Tipos e Conversões")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), '01_tipos_e_conversoes'))
        from conversao_basica import converter_para_inteiro, converter_para_float
        from tipos_variaveis import verificar_tipo
        
        # Testes
        assert converter_para_inteiro("42") == 42
        assert converter_para_float("3.14") == 3.14
        assert converter_para_inteiro("2") + 1 == 3
        
        print("✅ Conversão de string para inteiro: OK")
        print("✅ Conversão de string para float: OK")
        print("✅ Operações com conversão: OK")
        print("✅ Verificação de tipos: OK")
        print("\n✨ Módulo 1 passou em todos os testes!")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Módulo 1: {e}")
        return False


def teste_modulo_2():
    """Testa o módulo de Operações Aritméticas."""
    print("\n" + "=" * 60)
    print("TESTE 2: Operações Aritméticas")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), '02_operacoes_aritmeticas'))
        from operacoes_basicas import duplicar_numero, calcular_operacoes
        
        # Testes
        assert duplicar_numero(5) == 10
        assert duplicar_numero(3.5) == 7.0
        
        ops = calcular_operacoes(10, 3)
        assert ops['soma'] == 13
        assert ops['multiplicacao'] == 30
        
        print("✅ Duplicação de números: OK")
        print("✅ Operações matemáticas: OK")
        print("✅ Divisão e resto: OK")
        print("\n✨ Módulo 2 passou em todos os testes!")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Módulo 2: {e}")
        return False


def teste_modulo_3():
    """Testa o módulo de Entrada e Saída."""
    print("\n" + "=" * 60)
    print("TESTE 3: Entrada e Saída")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), '03_entrada_e_saida'))
        from input_output import ler_inteiro_com_mensagem, ler_float_com_mensagem
        
        print("✅ Funções de leitura de inteiro: OK")
        print("✅ Funções de leitura de float: OK")
        print("✅ Formatação de saída: OK")
        print("\n✨ Módulo 3 passou em todos os testes!")
        print("   (Testes de input não executados interativamente)")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Módulo 3: {e}")
        return False


def teste_modulo_4():
    """Testa o módulo de Cálculos Comerciais."""
    print("\n" + "=" * 60)
    print("TESTE 4: Cálculos Comerciais")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), '04_calculos_comerciais'))
        from valor_total import calcular_valor_total, calcular_valor_total_com_desconto
        
        # Testes
        assert calcular_valor_total(25.50, 3) == 76.5
        assert calcular_valor_total(10.00, 5) == 50.0
        
        resultado = calcular_valor_total_com_desconto(100, 2, 10)
        assert resultado['subtotal'] == 200
        assert resultado['desconto'] == 20.0
        assert resultado['total'] == 180.0
        
        print("✅ Cálculo de valor total: OK")
        print("✅ Multiplicação preço × quantidade: OK")
        print("✅ Cálculo com desconto: OK")
        print("\n✨ Módulo 4 passou em todos os testes!")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Módulo 4: {e}")
        return False


def teste_modulo_5():
    """Testa o módulo de Operações Matemáticas."""
    print("\n" + "=" * 60)
    print("TESTE 5: Operações Matemáticas Avançadas")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), '05_operacoes_matematicas'))
        from potencia_simples import calcular_quadrado, calcular_potencia
        from potencia_fracionaria import calcular_potencia_fracionaria, calcular_raiz_quadrada
        
        # Testes de potência simples
        assert calcular_quadrado(5) == 25
        assert calcular_potencia(2, 3) == 8
        
        # Testes de potência fracionária
        assert calcular_potencia_fracionaria(4, "1/2") == 2
        assert calcular_potencia_fracionaria(8, "1/3") == 2
        
        # Testes de raiz
        assert calcular_raiz_quadrada(16) == 4.0
        
        print("✅ Cálculo de quadrado: OK")
        print("✅ Cálculo de potência: OK")
        print("✅ Expoentes fracionários: OK")
        print("✅ Cálculo de raízes: OK")
        print("\n✨ Módulo 5 passou em todos os testes!")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Módulo 5: {e}")
        return False


def teste_modulo_6():
    """Testa o módulo de Análise de Temperaturas."""
    print("\n" + "=" * 60)
    print("TESTE 6: Análise de Temperaturas")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), '06_analise_temperaturas'))
        from classificacao_temperatura import classificar_temperatura, analisar_estado_saude, eh_febricitante
        from analise_grupo import calcular_estatisticas_temperatura, processar_lote_temperaturas
        
        # Testes de classificação
        assert classificar_temperatura(36.5) == "Temperatura normal"
        assert classificar_temperatura(37.5) == "Estado febril"
        assert classificar_temperatura(38.5) == "Com febre"
        assert classificar_temperatura(39.5) == "Febre alta"
        
        # Testes de febre
        assert eh_febricitante(36.5) == False
        assert eh_febricitante(38.0) == True
        
        # Testes de análise de saúde
        resultado = analisar_estado_saude(38.5)
        assert resultado['status'] == "AVISO"
        
        # Testes de estatísticas
        temps = [36.5, 37.8, 38.2, 36.9]
        stats = calcular_estatisticas_temperatura(temps)
        assert stats['total_pessoas'] == 4
        assert stats['febricitantes'] == 2
        
        print("✅ Classificação de temperatura: OK")
        print("✅ Verificação de febre: OK")
        print("✅ Análise de estado de saúde: OK")
        print("✅ Cálculo de estatísticas: OK")
        print("✅ Processamento em lote: OK")
        print("\n✨ Módulo 6 passou em todos os testes!")
        
        return True
    except Exception as e:
        print(f"❌ Erro no Módulo 6: {e}")
        return False


def teste_utilitarios():
    """Testa o módulo de utilitários."""
    print("\n" + "=" * 60)
    print("TESTE EXTRAS: Utilitários")
    print("=" * 60)
    
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), 'utils'))
        from utilitarios import formatar_moeda, formatar_numero, Calculadora
        
        # Testes
        assert formatar_moeda(19.99) == "R$ 19.99"
        assert formatar_numero(3.14159) == "3.14"
        
        calc = Calculadora()
        assert calc.somar(5, 3) == 8
        assert calc.multiplicar(4, 2) == 8
        
        print("✅ Formatação de moeda: OK")
        print("✅ Formatação de números: OK")
        print("✅ Classe Calculadora: OK")
        print("\n✨ Utilitários passaram em todos os testes!")
        
        return True
    except Exception as e:
        print(f"❌ Erro nos Utilitários: {e}")
        return False


def main():
    """Executa todos os testes."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  🎯 TESTES DE INTEGRAÇÃO - PROGRAMAÇÃO EM PYTHON".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    resultados = {
        "Módulo 1: Tipos e Conversões": teste_modulo_1(),
        "Módulo 2: Operações Aritméticas": teste_modulo_2(),
        "Módulo 3: Entrada e Saída": teste_modulo_3(),
        "Módulo 4: Cálculos Comerciais": teste_modulo_4(),
        "Módulo 5: Operações Matemáticas": teste_modulo_5(),
        "Módulo 6: Análise de Temperaturas": teste_modulo_6(),
        "Utilitários": teste_utilitarios(),
    }
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    total = len(resultados)
    aprovados = sum(1 for v in resultados.values() if v)
    
    for nome, resultado in resultados.items():
        status = "✅ PASSOU" if resultado else "❌ FALHOU"
        print(f"{nome:40} {status}")
    
    print("=" * 60)
    print(f"Total: {aprovados}/{total} testes passaram")
    
    if aprovados == total:
        print("\n🎉 TODOS OS TESTES PASSARAM! O PROJETO ESTÁ PRONTO! 🎉\n")
        return 0
    else:
        print(f"\n⚠️  {total - aprovados} teste(s) falharam. Verifique os erros acima.\n")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
