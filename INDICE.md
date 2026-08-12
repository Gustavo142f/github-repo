# 📚 ÍNDICE DO PROJETO

## 📖 Documentação (Comece por aqui!)

| Documento | Descrição |
|-----------|-----------|
| [README.md](README.md) | Visão geral do projeto e estrutura |
| [GUIA_EXECUCAO.md](GUIA_EXECUCAO.md) | Como executar cada módulo |
| [MAPEAMENTO_NOTEBOOK.md](MAPEAMENTO_NOTEBOOK.md) | Como o notebook foi organizado em módulos |
| [INDICE.md](INDICE.md) | Este arquivo |

---

## 🗂️ Módulos do Projeto

### 📌 Módulo 1: Tipos e Conversões
**Pasta:** [`01_tipos_e_conversoes/`](01_tipos_e_conversoes/)

Aprenda sobre conversão entre tipos e verificação de tipos.

| Arquivo | Função |
|---------|--------|
| `conversao_basica.py` | `converter_para_inteiro()`, `converter_para_float()`, `converter_para_string()` |
| `tipos_variaveis.py` | `verificar_tipo()`, `demonstrar_tipos()` |
| `exemplo_uso.py` | ✨ **Execute este arquivo** |

**Conceitos:**
- Conversão de string → int → float
- Operações aritméticas com conversão
- Verificação de tipos com `type()`

---

### 🔢 Módulo 2: Operações Aritméticas
**Pasta:** [`02_operacoes_aritmeticas/`](02_operacoes_aritmeticas/)

Operações matemáticas básicas e manipulação de números.

| Arquivo | Função |
|---------|--------|
| `operacoes_basicas.py` | `duplicar_numero()`, `calcular_operacoes()`, `somar_com_inteiro()` |
| `exemplo_uso.py` | ✨ **Execute este arquivo** |

**Conceitos:**
- Multiplicação de números
- Operações: +, -, *, /, %
- Casting de valores

---

### ⌨️ Módulo 3: Entrada e Saída
**Pasta:** [`03_entrada_e_saida/`](03_entrada_e_saida/)

Captura de dados do usuário e formatação de saída.

| Arquivo | Função |
|---------|--------|
| `input_output.py` | `ler_nome()`, `ler_numero()`, `ler_float()`, `ler_inteiro_com_mensagem()`, `exibir_nome()` |
| `exemplo_uso.py` | ✨ **Execute este arquivo** |

**Conceitos:**
- Função `input()` para capturar dados
- Conversão de entrada do usuário
- Formatação de saída com `print()`

---

### 💰 Módulo 4: Cálculos Comerciais
**Pasta:** [`04_calculos_comerciais/`](04_calculos_comerciais/)

Aplicação prática: cálculo de valor total em compras.

| Arquivo | Função |
|---------|--------|
| `valor_total.py` | `calcular_valor_total()`, `calcular_valor_total_com_desconto()`, `processar_compra()` |
| `exemplo_uso.py` | ✨ **Execute este arquivo** |

**Conceitos:**
- Cálculo: preço × quantidade
- Aplicações do mundo real
- Formatação de moeda

---

### 🧮 Módulo 5: Operações Matemáticas Avançadas
**Pasta:** [`05_operacoes_matematicas/`](05_operacoes_matematicas/)

Potências, raízes e uso da biblioteca `math`.

| Arquivo | Função |
|---------|--------|
| `potencia_simples.py` | `calcular_quadrado()`, `calcular_potencia()` |
| `potencia_fracionaria.py` | `calcular_potencia_fracionaria()`, `calcular_raiz_quadrada()`, `calcular_raiz_n()` |
| `exemplo_uso.py` | ✨ **Execute este arquivo** |

**Conceitos:**
- Uso da biblioteca `math`
- Potências: base^expoente
- Raízes quadradas e n-ésimas
- Expoentes fracionários

---

### 🌡️ Módulo 6: Análise de Temperaturas
**Pasta:** [`06_analise_temperaturas/`](06_analise_temperaturas/)

Loops, condicionais e aplicação prática em análise de saúde.

| Arquivo | Função |
|---------|--------|
| `classificacao_temperatura.py` | `classificar_temperatura()`, `analisar_estado_saude()`, `eh_febricitante()` |
| `analise_grupo.py` | `calcular_estatisticas_temperatura()`, `analisar_grupo_pessoas()`, `processar_lote_temperaturas()` |
| `exemplo_uso.py` | ✨ **Execute este arquivo** |

**Conceitos:**
- Loops: `for` e `while`
- Condicionais: `if`, `elif`, `else`
- Coleta de dados iterativa
- Cálculo de estatísticas e média
- Aplicação prática em análise de saúde

---

## 🛠️ Utilitários

**Pasta:** [`utils/`](utils/)

| Arquivo | Função |
|---------|--------|
| `utilitarios.py` | `formatar_moeda()`, `formatar_numero()`, `Calculadora` (classe) |

**Disponível em:** Todos os módulos

---

## 📁 Estrutura Completa

```
programacao-python/
│
├── 📂 01_tipos_e_conversoes/
│   ├── __init__.py
│   ├── conversao_basica.py
│   ├── tipos_variaveis.py
│   └── exemplo_uso.py
│
├── 📂 02_operacoes_aritmeticas/
│   ├── __init__.py
│   ├── operacoes_basicas.py
│   └── exemplo_uso.py
│
├── 📂 03_entrada_e_saida/
│   ├── __init__.py
│   ├── input_output.py
│   └── exemplo_uso.py
│
├── 📂 04_calculos_comerciais/
│   ├── __init__.py
│   ├── valor_total.py
│   └── exemplo_uso.py
│
├── 📂 05_operacoes_matematicas/
│   ├── __init__.py
│   ├── potencia_simples.py
│   ├── potencia_fracionaria.py
│   └── exemplo_uso.py
│
├── 📂 utils/
│   ├── __init__.py
│   └── utilitarios.py
│
├── 📄 README.md                    ← Comece aqui!
├── 📄 GUIA_EXECUCAO.md            ← Como rodar
├── 📄 MAPEAMENTO_NOTEBOOK.md       ← Notebook → Módulos
├── 📄 INDICE.md                    ← Este arquivo
├── 📄 main.py                      ← Testes de integração
└── 📄 requirements.txt             ← Dependências
```

---

## 🚀 Quick Start

### 1. Ver um exemplo
```bash
cd 01_tipos_e_conversoes
python exemplo_uso.py
```

### 2. Executar todos os testes
```bash
python main.py
```

### 3. Usar uma função em seu código
```python
from 04_calculos_comerciais.valor_total import calcular_valor_total

total = calcular_valor_total(25.50, 3)
print(total)  # 76.5
```

---

## 📋 Checklist de Aprendizado

### Tipos e Conversões ✅
- [ ] Entender `str`, `int`, `float`
- [ ] Converter entre tipos
- [ ] Usar `type()` para verificar tipo

### Operações Aritméticas ✅
- [ ] Realizar cálculos básicos
- [ ] Multiplicar e dividir
- [ ] Entender ordem de operações

### Entrada e Saída ✅
- [ ] Usar `input()` para ler dados
- [ ] Converter entrada do usuário
- [ ] Formatar saída com `print()`

### Cálculos Comerciais ✅
- [ ] Calcular valor total
- [ ] Aplicar descontos
- [ ] Trabalhar com valores monetários

### Matemática Avançada ✅
- [ ] Calcular potências
- [ ] Calcular raízes
- [ ] Usar a biblioteca `math`

---

## 🔗 Referências Rápidas

### Funções Principais

**Módulo 1:**
```python
converter_para_inteiro("42")
converter_para_float("3.14")
verificar_tipo(valor)
```

**Módulo 2:**
```python
duplicar_numero(5)
calcular_operacoes(a, b)
```

**Módulo 3:**
```python
ler_nome()
ler_numero()
ler_float_com_mensagem("Valor: ")
```

**Módulo 4:**
```python
calcular_valor_total(25.50, 3)
calcular_valor_total_com_desconto(100, 2, 10)
```

**Módulo 5:**
```python
calcular_quadrado(5)
calcular_potencia(2, 3)
calcular_potencia_fracionaria(4, "1/2")
calcular_raiz_quadrada(16)
calcular_raiz_n(8, 3)
```

---

## 📞 Suporte

### Erro: "ModuleNotFoundError"
- Certifique-se de estar no diretório correto
- Use: `cd 01_tipos_e_conversoes && python exemplo_uso.py`

### Erro: "SyntaxError"
- Verifique se está usando Python 3.8+
- Execute: `python --version`

### Erro: "No module named"
- Verifique se os arquivos `__init__.py` existem
- Revise o caminho da importação

---

## 💡 Dicas

1. **Execute os exemplos primeiro** - Veja o código funcionando
2. **Modifique os exemplos** - Mude valores e veja o que acontece
3. **Leia as docstrings** - Cada função tem documentação
4. **Use o MAPEAMENTO_NOTEBOOK.md** - Para entender a organização

---

## 📚 Próximos Passos

Depois de completar todos os módulos:

1. **Loops** - `for` e `while`
2. **Condicionais** - `if`, `else`, `elif`
3. **Strings Avançadas** - Manipulação e formatação
4. **Listas e Dicionários** - Estruturas de dados
5. **Funções** - Definir e usar funções
6. **Classes** - Programação Orientada a Objetos

---

## ✨ Características do Projeto

✅ **Código bem organizado** - Estrutura modular e semântica
✅ **Documentação completa** - Docstrings em cada função
✅ **Exemplos práticos** - Código executável em cada módulo
✅ **Tratamento de erros** - Validação de entrada
✅ **Reutilizável** - Funções para usar em seus projetos
✅ **PEP 8 compliant** - Segue padrões Python
✅ **Facilmente extensível** - Fácil de adicionar novos módulos

---

**Criado com ❤️ como Engenharia de Software Python**

*Última atualização: 2026-08-12*
