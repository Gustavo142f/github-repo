"""
Módulo de Operações Matemáticas Avançadas

Este módulo cobre:
- Uso da biblioteca math
- Cálculo de potências
- Expoentes fracionários
- Outras operações matemáticas avançadas
"""

from .potencia_simples import calcular_quadrado, calcular_potencia
from .potencia_fracionaria import calcular_potencia_fracionaria

__all__ = [
    'calcular_quadrado',
    'calcular_potencia',
    'calcular_potencia_fracionaria',
]
