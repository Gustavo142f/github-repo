"""
Módulo de Cálculos Comerciais

Este módulo cobre:
- Cálculo de valor total (preço unitário × quantidade)
- Operações com dados comerciais
- Aplicações do mundo real em vendas e compras
"""

from .valor_total import calcular_valor_total, calcular_valor_total_com_desconto

__all__ = [
    'calcular_valor_total',
    'calcular_valor_total_com_desconto',
]
