# 🚀 Guia de Execução

## Como Executar os Exemplos

Cada módulo possui um arquivo `exemplo_uso.py` que demonstra os conceitos aprendidos.

### Pré-requisitos

- Python 3.8 ou superior
- Terminal ou CMD

### Estrutura de Pastas

```
programacao-python/
├── 01_tipos_e_conversoes/
│   ├── __init__.py
│   ├── conversao_basica.py         # Funções de conversão
│   ├── tipos_variaveis.py          # Verificação de tipos
│   └── exemplo_uso.py              # ✨ EXECUTE AQUI
│
├── 02_operacoes_aritmeticas/
│   ├── __init__.py
│   ├── operacoes_basicas.py        # Operações matemáticas
│   └── exemplo_uso.py              # ✨ EXECUTE AQUI
│
├── 03_entrada_e_saida/
│   ├── __init__.py
│   ├── input_output.py             # Funções de I/O
│   └── exemplo_uso.py              # ✨ EXECUTE AQUI
│
├── 04_calculos_comerciais/
│   ├── __init__.py
│   ├── valor_total.py              # Cálculo de compras
│   └── exemplo_uso.py              # ✨ EXECUTE AQUI
│
├── 05_operacoes_matematicas/
│   ├── __init__.py
│   ├── potencia_simples.py         # Potências básicas
│   ├── potencia_fracionaria.py     # Raízes e expoentes
│   └── exemplo_uso.py              # ✨ EXECUTE AQUI
│
├── utils/
│   ├── __init__.py
│   └── utilitarios.py              # Funções auxiliares
│
├── README.md                        # Documentação
├── GUIA_EXECUCAO.md               # Este arquivo
└── requirements.txt                # Dependências
```

## Executando Cada Módulo

### 1️⃣ Tipos e Conversões

```bash
cd 01_tipos_e_conversoes
python exemplo_uso.py
```

**O que você aprenderá:**
- Conversão entre tipos (string → int → float)
- Verificação de tipos com `type()`
- Operações aritméticas com conversão

**Conteúdo:**
```python
texto = "2"           # String
int(texto)           # Converte para inteiro
float(texto)         # Converte para float
1 + int(texto)       # Soma com conversão
```

---

### 2️⃣ Operações Aritméticas

```bash
cd 02_operacoes_aritmeticas
python exemplo_uso.py
```

**O que você aprenderá:**
- Multiplicação e duplicação de números
- Operações matemáticas básicas (+, -, *, /)
- Resto da divisão (%)

**Conteúdo:**
```python
numero * 2           # Duplicação
a + b, a - b, a * b  # Operações básicas
```

---

### 3️⃣ Entrada e Saída

```bash
cd 03_entrada_e_saida
python exemplo_uso.py
```

**O que você aprenderá:**
- Captura de dados com `input()`
- Conversão de entrada do usuário
- Formatação de saída com `print()`

**Conteúdo:**
```python
nome = input("Digite seu nome: ")
numero = int(input("Digite um número: "))
print("Resultado:", valor)
```

**Para usar com entrada interativa:**
Descomente as linhas com `input()` no código.

---

### 4️⃣ Cálculos Comerciais

```bash
cd 04_calculos_comerciais
python exemplo_uso.py
```

**O que você aprenderá:**
- Cálculo de valor total (preço × quantidade)
- Aplicações do mundo real
- Formatação de moeda

**Conteúdo:**
```python
valor_unitario = 25.50
quantidade = 3
valor_total = valor_unitario * quantidade
```

---

### 5️⃣ Operações Matemáticas Avançadas

```bash
cd 05_operacoes_matematicas
python exemplo_uso.py
```

**O que você aprenderá:**
- Uso da biblioteca `math`
- Cálculo de potências (base^expoente)
- Raízes quadradas e n-ésimas
- Expoentes fracionários

**Conteúdo:**
```python
import math
math.pow(base, expoente)        # Potência
math.sqrt(numero)               # Raiz quadrada
16 ** (1/2)                     # Raiz quadrada (alternativa)
```

---

## Executando Todos os Módulos

### No Windows (CMD ou PowerShell):

```batch
cd 01_tipos_e_conversoes && python exemplo_uso.py && cd ..
cd 02_operacoes_aritmeticas && python exemplo_uso.py && cd ..
cd 03_entrada_e_saida && python exemplo_uso.py && cd ..
cd 04_calculos_comerciais && python exemplo_uso.py && cd ..
cd 05_operacoes_matematicas && python exemplo_uso.py
```

### No Linux/macOS (Bash):

```bash
for dir in 0*/; do
    echo "Executando $dir..."
    cd "$dir" && python exemplo_uso.py && cd ..
done
```

---

## Importando Módulos em Seus Próprios Projetos

Se quiser usar as funções dos módulos em outros arquivos:

```python
# Importar tudo de um módulo
from 01_tipos_e_conversoes.conversao_basica import converter_para_inteiro

# Usar a função
numero = converter_para_inteiro("42")
print(numero)

# Ou importar múltiplas funções
from 04_calculos_comerciais.valor_total import (
    calcular_valor_total,
    calcular_valor_total_com_desconto
)
```

---

## 📚 Conceitos Progressivos

Os módulos estão organizados de forma progressiva:

1. **Tipos e Conversões** → Fundação
2. **Operações Aritméticas** → Cálculos básicos
3. **Entrada e Saída** → Interação com usuário
4. **Cálculos Comerciais** → Aplicação prática
5. **Matemática Avançada** → Conceitos avançados

---

## 🐛 Dicas de Resolução de Problemas

### Erro: `ModuleNotFoundError: No module named...`

**Solução:** Certifique-se de estar no diretório correto:
```bash
# ✅ Correto
cd 01_tipos_e_conversoes && python exemplo_uso.py

# ❌ Errado
python 01_tipos_e_conversoes/exemplo_uso.py
```

### Erro: `SyntaxError` ou `IndentationError`

**Solução:** Verifique se está usando Python 3.8+:
```bash
python --version
```

### Erro: `ZeroDivisionError`

**Solução:** Evite dividir por zero. O código já trata disso:
```python
if denominador != 0:
    resultado = numerador / denominador
```

---

## 🎯 Próximos Passos

Depois de dominar esses módulos, você pode explorar:

- 🔄 **Loops** (`for`, `while`)
- 🔀 **Condicionais** (`if`, `else`, `elif`)
- 📝 **Strings** (manipulação e formatação)
- 📊 **Listas** e **Dicionários**
- 🎯 **Funções** (definição e uso)
- 📦 **Classes** (Programação Orientada a Objetos)

---

## ✉️ Contato e Suporte

Se encontrar erros ou tiver dúvidas:

1. Verifique o arquivo `README.md`
2. Revise o código do módulo
3. Experimente modificar os exemplos
4. Consulte a [documentação oficial do Python](https://docs.python.org/)

---

**Bom aprendizado! 🚀📚**
