# 📊 Mapeamento: Notebook → Módulos

Este arquivo documenta como o conteúdo original do Notebook foi organizado em módulos Python.

## Células do Notebook Original

### Célula 1-3: Conversão de Tipos

**Código Original:**
```python
texto = "2"
texto1= str(2);
texto2 = float(2) #Declaração explícita de variável

print(texto)
print(texto1)
print(texto2)

soma = 1 + int(texto)
print(soma)

textoTransformado = int(texto)
soma = 1 + textoTransformado
print(soma)

soma = 1 + texto2
print(soma)
```

**Organizado em:** `01_tipos_e_conversoes/`
- **Módulo:** `conversao_basica.py`
  - `converter_para_inteiro()`
  - `converter_para_float()`
  - `converter_para_string()`
- **Módulo:** `tipos_variaveis.py`
  - `verificar_tipo()`
  - `demonstrar_tipos()`

---

### Célula 4: Input de Número

**Código Original:**
```python
a = int(input("Digite um número:"))
b = a * 2
print(b)

type(a)
```

**Organizado em:** `02_operacoes_aritmeticas/`
- **Módulo:** `operacoes_basicas.py`
  - `duplicar_numero()`
  - `somar_com_inteiro()`

**Também em:** `03_entrada_e_saida/`
- **Módulo:** `input_output.py`
  - `ler_numero()`
  - `ler_inteiro_com_mensagem()`

---

### Célula 5: Verificação de Tipos

**Código Original:**
```python
print(type(texto))

print(texto)
print(texto1)
```

**Organizado em:** `01_tipos_e_conversoes/`
- **Módulo:** `tipos_variaveis.py`
  - `verificar_tipo()`

---

### Célula 6: Diferentes Declarações de Números

**Código Original:**
```python
numero= 3
numero1= int(3)
mumero2= float(3)
numero3= 3.0

print(numero)
print(numero1)
print(mumero2)
print(numero3)
```

**Organizado em:** `01_tipos_e_conversoes/`
- **Módulo:** `tipos_variaveis.py`
  - `demonstrar_tipos()`

---

### Célula 7: Input de Nome

**Código Original:**
```python
nome= input("Digite o seu nome: ")
print("O seu nome é: ", nome)
```

**Organizado em:** `03_entrada_e_saida/`
- **Módulo:** `input_output.py`
  - `ler_nome()`
  - `exibir_nome()`

---

### Célula 8-10: Cálculo de Valor Total

**Código Original:**
```python
valor_uni= float(input("Informe o valor unitário: "))
quantidade= int(input("Informe a quantidade de produtos: "))
valor_total = valor_uni*quantidade
print("O total da compra é:", valor_total)

valor_uni= float(input("Informe o valor unitário: "))
quantidade= int(input("Informe a quantidade de produtos: "))
valor_total = valor_uni*quantidade
print("O total da compra é: ", valor_total)

valor_total= valor_uni*quantidade
print("O total da compra é: ", valor_total)
```

**Organizado em:** `04_calculos_comerciais/`
- **Módulo:** `valor_total.py`
  - `calcular_valor_total()`
  - `calcular_valor_total_com_desconto()`
  - `processar_compra()`

**Também em:** `03_entrada_e_saida/`
- **Módulo:** `input_output.py`
  - `ler_float_com_mensagem()`

---

### Célula 11: Potência Simples

**Código Original:**
```python
import math

numero1= int(input("Informe um número inteiro: "))
quadrado= int(math.pow(numero1,2)) #onde mat.pow(base,expoente)
print("O quadrado do número informado é: ", quadrado)
```

**Organizado em:** `05_operacoes_matematicas/`
- **Módulo:** `potencia_simples.py`
  - `calcular_quadrado()`
  - `calcular_potencia()`
  - `calcular_potencia_com_validacao()`

---

### Célula 12: Potência com Expoente Fracionário

**Código Original:**
```python
import math

numero1= int(input("Informe um número inteiro: "))
expoente_str= input("Informe o expoente: ")

if '/' in expoente_str:
    numerator, denominator = map(float, expoente_str.split('/'))
    expoente = numerator / denominator
else:
    expoente = float(expoente_str)

potencia= int(math.pow(numero1,expoente)) #onde mat.pow(base,expoente)
print("A potência do número informado é: ", potencia)
```

**Organizado em:** `05_operacoes_matematicas/`
- **Módulo:** `potencia_fracionaria.py`
  - `calcular_potencia_fracionaria()`
  - `calcular_raiz_quadrada()`
  - `calcular_raiz_n()`

---

## Estrutura de Organização

```
Conteúdo Original          Organização em Módulos
─────────────────          ──────────────────────

Tipos                 →    01_tipos_e_conversoes/
                           ├── conversao_basica.py
                           └── tipos_variaveis.py

Input/Output          →    03_entrada_e_saida/
                           └── input_output.py

Operações Simples     →    02_operacoes_aritmeticas/
                           └── operacoes_basicas.py

Aplicação Comercial   →    04_calculos_comerciais/
                           └── valor_total.py

Matemática Avançada   →    05_operacoes_matematicas/
                           ├── potencia_simples.py
                           └── potencia_fracionaria.py
```

---

## Melhorias Implementadas

### ✨ Funcionalidades Adicionadas

| Aspecto | Original | Melhorado |
|---------|----------|-----------|
| **Funções** | Código solto | Funções reutilizáveis com docstrings |
| **Tratamento de Erros** | Nenhum | Try/except implementado |
| **Documentação** | Ausente | Docstrings com exemplos |
| **Validação** | Nenhuma | Validação de entrada e tipos |
| **Exemplos** | Exemplos embutidos | Exemplos organizados em arquivos separados |
| **Reutilização** | Código duplicado | Funções modulares |
| **Organização** | Monolítico | Estrutura por tema |
| **Formatação** | print() básico | Formatação customizável |

---

## Como Usar Este Mapeamento

Se você quer:

1. **Encontrar um código específico do notebook**
   - Procure pela célula acima
   - Veja em qual módulo foi organizado
   - Abra o arquivo correspondente

2. **Executar um exemplo**
   - Vá para o módulo
   - Execute `python exemplo_uso.py`

3. **Usar as funções em novo código**
   - Importe do módulo apropriado
   - Use as funções documentadas

4. **Estender/Modificar o código**
   - Edite os arquivos `.py` individuais
   - Cada função é independente e testável

---

## Referência Rápida de Funções

### 01_tipos_e_conversoes
```python
converter_para_inteiro("42")          # → 42
converter_para_float("3.14")          # → 3.14
verificar_tipo(42)                    # → <class 'int'>
```

### 02_operacoes_aritmeticas
```python
duplicar_numero(5)                    # → 10
calcular_operacoes(10, 3)             # → {'+': 13, '-': 7, '*': 30, ...}
somar_com_inteiro("2")                # → 3
```

### 03_entrada_e_saida
```python
ler_nome()                            # Lê nome do usuário
ler_numero()                          # Lê número inteiro
ler_float_com_mensagem("Valor: ")     # Lê float com mensagem
```

### 04_calculos_comerciais
```python
calcular_valor_total(25.50, 3)        # → 76.5
calcular_valor_total_com_desconto(100, 2, 10)  # → {subtotal, desconto, total}
processar_compra(19.90, 4)            # → Retorna dict formatado
```

### 05_operacoes_matematicas
```python
calcular_quadrado(5)                  # → 25
calcular_potencia(2, 3)               # → 8
calcular_potencia_fracionaria(16, "1/2")  # → 4
calcular_raiz_quadrada(16)            # → 4.0
calcular_raiz_n(8, 3)                 # → 2.0
```

---

**Estrutura criada com princípios de Engenharia de Software! 🏗️**
