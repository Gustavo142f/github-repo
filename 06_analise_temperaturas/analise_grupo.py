"""
Análise de Grupo de Pessoas

Funções para coletar e analisar temperaturas de um grupo.
Demonstra uso de loops e cálculo de estatísticas.
"""

from .classificacao_temperatura import classificar_temperatura, eh_febricitante


def calcular_estatisticas_temperatura(temperaturas):
    """
    Calcula estatísticas de um conjunto de temperaturas.
    
    Args:
        temperaturas (list): Lista de temperaturas em Celsius
        
    Returns:
        dict: Dicionário com estatísticas
        
    Exemplo:
        >>> temps = [36.5, 37.8, 38.2, 36.9]
        >>> stats = calcular_estatisticas_temperatura(temps)
        >>> stats['media']
        37.35
    """
    if not temperaturas:
        return None
    
    soma = sum(temperaturas)
    media = soma / len(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_maxima = max(temperaturas)
    
    # Contar febricitantes
    febricitantes = sum(1 for t in temperaturas if eh_febricitante(t))
    
    return {
        'soma': soma,
        'media': round(media, 2),
        'minima': temperatura_minima,
        'maxima': temperatura_maxima,
        'total_pessoas': len(temperaturas),
        'febricitantes': febricitantes,
        'normais': len(temperaturas) - febricitantes,
        'percentual_febricitantes': round((febricitantes / len(temperaturas)) * 100, 2),
    }


def analisar_grupo_pessoas(quantidade=None, temperaturas=None):
    """
    Analisa um grupo de pessoas coletando suas temperaturas.
    
    Pode ser usado de duas formas:
    1. Com quantidade: Coleta dados via input()
    2. Com lista de temperaturas: Analisa dados já coletados
    
    Args:
        quantidade (int, optional): Número de pessoas a analisar
        temperaturas (list, optional): Lista de temperaturas já coletadas
        
    Returns:
        dict: Análise completa do grupo
        
    Exemplo:
        >>> # Modo 1: Coletar dados
        >>> # resultado = analisar_grupo_pessoas(quantidade=3)
        
        >>> # Modo 2: Analisar dados existentes
        >>> temps = [36.5, 37.8, 38.2]
        >>> resultado = analisar_grupo_pessoas(temperaturas=temps)
        >>> resultado['media']
        37.5
    """
    # Modo 1: Coletar dados do usuário
    if quantidade is not None and temperaturas is None:
        temperaturas = []
        print(f"\n{'='*50}")
        print(f"Análise de Temperatura de {quantidade} Pessoa(s)")
        print(f"{'='*50}\n")
        
        for i in range(quantidade):
            while True:
                try:
                    temp_input = input(f"Pessoa {i+1} - Digite a temperatura (°C): ")
                    temperatura = float(temp_input)
                    
                    if temperatura < 30 or temperatura > 45:
                        print("❌ Temperatura inválida. Use valores entre 30 e 45°C")
                        continue
                    
                    temperaturas.append(temperatura)
                    classificacao = classificar_temperatura(temperatura)
                    print(f"   → {classificacao}\n")
                    break
                except ValueError:
                    print("❌ Entrada inválida. Digite um número.")
    
    # Modo 2: Analisar dados fornecidos
    elif temperaturas is not None:
        if not temperaturas:
            return {"erro": "Lista de temperaturas vazia"}
    
    else:
        return {"erro": "Forneça quantidade ou lista de temperaturas"}
    
    # Calcular estatísticas
    stats = calcular_estatisticas_temperatura(temperaturas)
    
    return {
        'temperaturas': temperaturas,
        'stats': stats,
        'resumo': gerar_resumo_analise(stats),
    }


def gerar_resumo_analise(stats):
    """
    Gera um resumo textual da análise.
    
    Args:
        stats (dict): Estatísticas calculadas
        
    Returns:
        str: Resumo formatado
    """
    if not stats:
        return "Nenhum dado para analisar"
    
    resumo = f"""
╔══════════════════════════════════════╗
║         ANÁLISE DE TEMPERATURAS      ║
╚══════════════════════════════════════╝

📊 Estatísticas:
  • Total de pessoas analisadas: {stats['total_pessoas']}
  • Temperatura média: {stats['media']}°C
  • Temperatura mínima: {stats['minima']}°C
  • Temperatura máxima: {stats['maxima']}°C

🏥 Saúde:
  • Pessoas com febre: {stats['febricitantes']} ({stats['percentual_febricitantes']}%)
  • Pessoas normais: {stats['normais']} ({100 - stats['percentual_febricitantes']}%)
"""
    return resumo


def processar_lote_temperaturas(lista_temperaturas, mostrar_detalhes=False):
    """
    Processa um lote de temperaturas já coletadas.
    
    Args:
        lista_temperaturas (list): Lista de temperaturas
        mostrar_detalhes (bool): Se deve mostrar análise detalhada
        
    Returns:
        dict: Análise completa
        
    Exemplo:
        >>> temps = [36.5, 37.8, 38.2, 36.9, 37.1]
        >>> resultado = processar_lote_temperaturas(temps, mostrar_detalhes=True)
    """
    resultado = {
        'temperaturas': lista_temperaturas,
        'stats': calcular_estatisticas_temperatura(lista_temperaturas),
        'detalhes': []
    }
    
    if mostrar_detalhes:
        for i, temp in enumerate(lista_temperaturas, 1):
            classificacao = classificar_temperatura(temp)
            resultado['detalhes'].append({
                'pessoa': i,
                'temperatura': temp,
                'classificacao': classificacao,
            })
    
    return resultado
