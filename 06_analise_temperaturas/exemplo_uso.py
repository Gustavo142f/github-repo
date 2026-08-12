"""
Exemplo de Uso - Análise de Temperaturas

Demonstra classificação de temperaturas e análise de grupos.

NOTA: Este script foi adaptado para fins de demonstração.
Em um uso real, descomente as linhas com input().
"""

from classificacao_temperatura import classificar_temperatura, analisar_estado_saude, eh_febricitante
from analise_grupo import analisar_grupo_pessoas, calcular_estatisticas_temperatura, processar_lote_temperaturas


def exemplo_classificacao_individual():
    """Exemplo de classificação de uma temperatura individual."""
    print("=" * 60)
    print("EXEMPLO 1: Classificação Individual de Temperatura")
    print("=" * 60 + "\n")
    
    temperaturas_teste = [
        36.5,   # Normal
        37.0,   # Normal
        37.5,   # Febril
        38.0,   # Febril
        38.5,   # Com febre
        39.0,   # Com febre
        39.5,   # Febre alta
        40.0,   # Febre alta
    ]
    
    for temp in temperaturas_teste:
        classificacao = classificar_temperatura(temp)
        print(f"Temperatura: {temp}°C → {classificacao}")
    
    print()


def exemplo_estado_saude():
    """Exemplo de análise completa de estado de saúde."""
    print("\n" + "=" * 60)
    print("EXEMPLO 2: Análise Completa de Estado de Saúde")
    print("=" * 60 + "\n")
    
    temperaturas_teste = [36.5, 37.5, 38.5, 39.5]
    
    for temp in temperaturas_teste:
        resultado = analisar_estado_saude(temp)
        print(f"Temperatura: {temp}°C")
        print(f"  Classificação: {resultado['classificacao']}")
        print(f"  Status: {resultado['status']}")
        print(f"  Recomendação: {resultado['recomendacao']}\n")


def exemplo_febricitante():
    """Exemplo de verificação de febre."""
    print("\n" + "=" * 60)
    print("EXEMPLO 3: Verificação de Febre")
    print("=" * 60 + "\n")
    
    temperaturas_teste = [36.5, 37.0, 37.2, 38.0, 39.0]
    
    for temp in temperaturas_teste:
        tem_febre = eh_febricitante(temp)
        status = "🔴 COM FEBRE" if tem_febre else "🟢 NORMAL"
        print(f"Temperatura: {temp}°C → {status}")
    
    print()


def exemplo_analise_grupo():
    """Exemplo de análise de grupo com dados de demonstração."""
    print("\n" + "=" * 60)
    print("EXEMPLO 4: Análise de Grupo de Pessoas")
    print("=" * 60 + "\n")
    
    # Dados de demonstração
    temperaturas = [36.5, 37.8, 38.2, 36.9, 37.1, 39.2, 38.0, 37.5]
    
    print(f"Analisando {len(temperaturas)} pessoas...\n")
    
    resultado = analisar_grupo_pessoas(temperaturas=temperaturas)
    
    # Mostrar análise
    print(resultado['resumo'])
    
    # Mostrar detalhes
    print("\n📋 Detalhes Individuais:")
    for i, temp in enumerate(resultado['temperaturas'], 1):
        classificacao = classificar_temperatura(temp)
        febre = "🔴 FEBRE" if eh_febricitante(temp) else "🟢"
        print(f"  Pessoa {i:2d}: {temp}°C → {classificacao:20s} {febre}")
    
    print()


def exemplo_estatisticas():
    """Exemplo de cálculo de estatísticas."""
    print("\n" + "=" * 60)
    print("EXEMPLO 5: Estatísticas Detalhadas")
    print("=" * 60 + "\n")
    
    temperaturas = [36.5, 37.8, 38.2, 36.9, 37.1, 39.2, 38.0, 37.5]
    
    stats = calcular_estatisticas_temperatura(temperaturas)
    
    print("Estatísticas Calculadas:")
    print(f"  • Soma total: {stats['soma']:.2f}°C")
    print(f"  • Média: {stats['media']}°C")
    print(f"  • Mínima: {stats['minima']}°C")
    print(f"  • Máxima: {stats['maxima']}°C")
    print(f"  • Total de pessoas: {stats['total_pessoas']}")
    print(f"  • Com febre: {stats['febricitantes']}")
    print(f"  • Normais: {stats['normais']}")
    print(f"  • Percentual com febre: {stats['percentual_febricitantes']}%\n")


def exemplo_processamento_lote():
    """Exemplo de processamento em lote."""
    print("\n" + "=" * 60)
    print("EXEMPLO 6: Processamento em Lote com Detalhes")
    print("=" * 60 + "\n")
    
    temperaturas = [36.5, 37.8, 38.2, 36.9]
    
    resultado = processar_lote_temperaturas(temperaturas, mostrar_detalhes=True)
    
    print("Análise Detalhada por Pessoa:")
    for detalhe in resultado['detalhes']:
        print(f"  Pessoa {detalhe['pessoa']}: {detalhe['temperatura']}°C → {detalhe['classificacao']}")
    
    print(f"\nMédia do grupo: {resultado['stats']['media']}°C")
    print()


def exemplo_uso_interativo():
    """
    Exemplo de uso interativo (para usar com input real).
    Descomente para usar com entrada do usuário.
    """
    print("\n" + "=" * 60)
    print("EXEMPLO 7: Modo Interativo (Descomente para usar)")
    print("=" * 60 + "\n")
    
    print("Para usar o modo interativo, descomente as linhas abaixo:")
    print("""
# quantidade = int(input("Quantas pessoas serão analisadas? "))
# resultado = analisar_grupo_pessoas(quantidade=quantidade)
# print(resultado['resumo'])
    """)


if __name__ == "__main__":
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  EXEMPLOS - ANÁLISE DE TEMPERATURAS".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    
    exemplo_classificacao_individual()
    exemplo_estado_saude()
    exemplo_febricitante()
    exemplo_analise_grupo()
    exemplo_estatisticas()
    exemplo_processamento_lote()
    exemplo_uso_interativo()
    
    print("\n" + "=" * 60)
    print("MODO INTERATIVO")
    print("=" * 60 + "\n")
    print("Para usar com entrada de dados real do usuário:")
    print()
    print("  quantidade = int(input('Quantas pessoas? '))")
    print("  resultado = analisar_grupo_pessoas(quantidade=quantidade)")
    print("  print(resultado['resumo'])")
    print()
