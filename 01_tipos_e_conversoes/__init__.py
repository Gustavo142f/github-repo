"""
Módulo de Tipos e Conversões

Este módulo cobre:
- Conversão explícita entre tipos primitivos
- Verificação de tipos com type()
- Boas práticas em declaração de variáveis
"""

from .conversao_basica import converter_para_inteiro, converter_para_float, converter_para_string
from .tipos_variaveis import verificar_tipo, demonstrar_tipos

__all__ = [
    'converter_para_inteiro',
    'converter_para_float',
    'converter_para_string',
    'verificar_tipo',
    'demonstrar_tipos',
]
