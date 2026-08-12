"""
Classificação de Temperatura

Funções para classificar temperaturas corpóreas
de acordo com padrões médicos.
"""


def classificar_temperatura(temperatura):
    """
    Classifica a temperatura corpórea em categorias.
    
    Categorias:
    - Normal: < 37.2°C
    - Febril: 37.2°C a 38°C
    - Com febre: 38°C a 39°C
    - Febre alta: >= 39°C
    
    Args:
        temperatura (float): Temperatura em Celsius
        
    Returns:
        str: Classificação da temperatura
        
    Exemplo:
        >>> classificar_temperatura(36.5)
        'Temperatura normal'
        >>> classificar_temperatura(38.5)
        'Com febre'
    """
    if temperatura < 37.2:
        return "Temperatura normal"
    elif temperatura <= 38:
        return "Estado febril"
    elif temperatura <= 39:
        return "Com febre"
    else:
        return "Febre alta"


def analisar_estado_saude(temperatura):
    """
    Analisa o estado de saúde baseado na temperatura.
    
    Args:
        temperatura (float): Temperatura em Celsius
        
    Returns:
        dict: Dicionário com informações da saúde
        
    Exemplo:
        >>> resultado = analisar_estado_saude(37.8)
        >>> resultado['classificacao']
        'Estado febril'
    """
    classificacao = classificar_temperatura(temperatura)
    
    # Determinar recomendação
    if temperatura < 36:
        recomendacao = "Procure um médico - Hipotermia"
        status = "CRÍTICO"
    elif temperatura < 37.2:
        recomendacao = "Tudo normal"
        status = "SAUDÁVEL"
    elif temperatura < 38:
        recomendacao = "Repouso recomendado"
        status = "ATENÇÃO"
    elif temperatura < 39:
        recomendacao = "Procure um médico"
        status = "AVISO"
    else:
        recomendacao = "Procure urgentemente um médico"
        status = "CRÍTICO"
    
    return {
        'temperatura': temperatura,
        'classificacao': classificacao,
        'recomendacao': recomendacao,
        'status': status,
    }


def eh_febricitante(temperatura):
    """
    Verifica se a pessoa está com febre.
    
    Args:
        temperatura (float): Temperatura em Celsius
        
    Returns:
        bool: True se temperatura >= 37.2
        
    Exemplo:
        >>> eh_febricitante(38.5)
        True
        >>> eh_febricitante(36.5)
        False
    """
    return temperatura >= 37.2
