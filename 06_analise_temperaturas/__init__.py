"""
Módulo de Análise de Temperaturas

Este módulo cobre:
- Loops (for, while)
- Condicionais (if, elif, else)
- Coleta de dados do usuário
- Cálculo de média
- Classificação de temperaturas
- Aplicação prática em saúde
"""

from .classificacao_temperatura import classificar_temperatura, analisar_estado_saude
from .analise_grupo import analisar_grupo_pessoas, calcular_estatisticas_temperatura

__all__ = [
    'classificar_temperatura',
    'analisar_estado_saude',
    'analisar_grupo_pessoas',
    'calcular_estatisticas_temperatura',
]
