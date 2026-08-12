# 🐍 Programação em Python - Módulos Organizados

Uma estrutura profissional e modular de código Python, organizando conteúdo de aprendizado em 5 módulos temáticos com documentação completa, exemplos práticos e tratamento de erros.

[![GitHub](https://img.shields.io/badge/GitHub-Gustavo142f-blue?logo=github)](https://github.com/Gustavo142f/github-repo)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success)](https://github.com/Gustavo142f/github-repo)

---

## 📚 Módulos Disponíveis

### 1️⃣ [Tipos e Conversões](01_tipos_e_conversoes/)
Aprenda conversão entre tipos primitivos e verificação de tipos.
- `str` → `int` → `float`
- Função `type()` para verificação
- Operações aritméticas com conversão

**Executar:** `python 01_tipos_e_conversoes/exemplo_uso.py`

---

### 2️⃣ [Operações Aritméticas](02_operacoes_aritmeticas/)
Operações matemáticas básicas e manipulação de números.
- Multiplicação e duplicação
- Operações: `+`, `-`, `*`, `/`, `%`
- Casting de valores

**Executar:** `python 02_operacoes_aritmeticas/exemplo_uso.py`

---

### 3️⃣ [Entrada e Saída](03_entrada_e_saida/)
Captura de dados e formatação de saída.
- Função `input()` para capturar dados
- Conversão de entrada
- Formatação com `print()`

**Executar:** `python 03_entrada_e_saida/exemplo_uso.py`

---

### 4️⃣ [Cálculos Comerciais](04_calculos_comerciais/)
Aplicação prática: sistema de compras.
- Cálculo: preço × quantidade
- Desconto e valor final
- Formatação de moeda

**Executar:** `python 04_calculos_comerciais/exemplo_uso.py`

---

### 5️⃣ [Operações Matemáticas Avançadas](05_operacoes_matematicas/)
Potências, raízes e uso da biblioteca `math`.
- Potência: `base^expoente`
- Raízes quadradas e n-ésimas
- Expoentes fracionários

**Executar:** `python 05_operacoes_matematicas/exemplo_uso.py`

---

## 🚀 Quick Start

### Instalação

```bash
# Clone o repositório
git clone https://github.com/Gustavo142f/github-repo.git
cd github-repo

# Não há dependências externas!
# Python 3.8+ é suficiente
```

### Executar Exemplos

```bash
# Executar um módulo específico
cd 01_tipos_e_conversoes
python exemplo_uso.py

# Ou execute todos os testes
python main.py
```

### Usar em seu Projeto

```python
from 04_calculos_comerciais.valor_total import calcular_valor_total

# Calcular valor total
total = calcular_valor_total(25.50, 3)
print(f"Total: R$ {total:.2f}")  # Total: R$ 76.50
```

---

## 📁 Estrutura do Projeto

```
programacao-python/
├── 01_tipos_e_conversoes/          # Conversão de tipos
│   ├── conversao_basica.py
│   ├── tipos_variaveis.py
│   └── exemplo_uso.py
├── 02_operacoes_aritmeticas/       # Operações matemáticas
│   ├── operacoes_basicas.py
│   └── exemplo_uso.py
├── 03_entrada_e_saida/             # Input/Output
│   ├── input_output.py
│   └── exemplo_uso.py
├── 04_calculos_comerciais/         # Aplicação prática
│   ├── valor_total.py
│   └── exemplo_uso.py
├── 05_operacoes_matematicas/       # Matemática avançada
│   ├── potencia_simples.py
│   ├── potencia_fracionaria.py
│   └── exemplo_uso.py
├── utils/                           # Utilitários compartilhados
│   ├── __init__.py
│   └── utilitarios.py
├── 📖 README.md                     # Este arquivo
├── 📖 GUIA_EXECUCAO.md             # Como rodar
├── 📖 MAPEAMENTO_NOTEBOOK.md       # Organização do código
├── 📖 INDICE.md                    # Índice completo
├── main.py                          # Testes de integração
└── requirements.txt                 # Dependências
```

---

## 📚 Documentação Completa

| Documento | Descrição |
|-----------|-----------|
| [README.md](README.md) | Visão geral do projeto |
| [GUIA_EXECUCAO.md](GUIA_EXECUCAO.md) | Instruções detalhadas de execução |
| [INDICE.md](INDICE.md) | Índice completo e navegação |
| [MAPEAMENTO_NOTEBOOK.md](MAPEAMENTO_NOTEBOOK.md) | Como o código foi organizado |
| [DEPLOY_GITHUB.md](DEPLOY_GITHUB.md) | Como fazer deploy (se necessário) |

---

## 💡 Funcionalidades

✅ **Código bem organizado** - Estrutura modular e semântica  
✅ **Documentação completa** - Docstrings em cada função  
✅ **Exemplos práticos** - Código executável em cada módulo  
✅ **Tratamento de erros** - Validação de entrada com try/except  
✅ **Reutilizável** - Funções independentes para usar em seus projetos  
✅ **PEP 8 compliant** - Segue padrões Python  
✅ **Sem dependências** - Usa apenas biblioteca padrão do Python  

---

## 🎯 Exemplos de Uso

### Exemplo 1: Converter e Somar
```python
from 01_tipos_e_conversoes.conversao_basica import converter_para_inteiro

texto = "42"
numero = converter_para_inteiro(texto)
resultado = numero + 1
print(resultado)  # 43
```

### Exemplo 2: Calcular Valor Total
```python
from 04_calculos_comerciais.valor_total import calcular_valor_total

valor = calcular_valor_total(25.50, 3)
print(f"Total: R$ {valor:.2f}")  # Total: R$ 76.50
```

### Exemplo 3: Potência Fracionária
```python
from 05_operacoes_matematicas.potencia_fracionaria import calcular_potencia_fracionaria

resultado = calcular_potencia_fracionaria(16, "1/2")  # Raiz quadrada
print(resultado)  # 4
```

---

## 🔧 Requisitos

- **Python:** 3.8 ou superior
- **Sistema Operacional:** Windows, macOS, Linux
- **Dependências:** Nenhuma! (usa apenas biblioteca padrão)

---

## 📋 Checklist de Aprendizado

- [ ] Tipos e Conversões
- [ ] Operações Aritméticas
- [ ] Entrada e Saída
- [ ] Cálculos Comerciais
- [ ] Operações Matemáticas Avançadas

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named...`
**Solução:** Certifique-se de estar no diretório correto:
```bash
cd 01_tipos_e_conversoes
python exemplo_uso.py
```

### `SyntaxError` ou `IndentationError`
**Solução:** Verifique se está usando Python 3.8+:
```bash
python --version
```

### `ZeroDivisionError`
**Solução:** Não divida por zero. O código já trata disso em operações.

---

## 🚀 Próximos Passos

Depois de dominar os módulos:
1. 🔄 Loops (`for`, `while`)
2. 🔀 Condicionais (`if`, `else`, `elif`)
3. 📝 Strings (manipulação avançada)
4. 📊 Listas e Dicionários
5. 🎯 Funções (definição e escopo)
6. 📦 Classes (Programação Orientada a Objetos)

---

## 📝 Contribuindo

Sinta-se livre para:
- Reportar bugs em Issues
- Sugerir novos módulos
- Melhorar a documentação
- Adicionar mais exemplos

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

---

## 👤 Autor

**Gustavo142f**
- 🔗 GitHub: [@Gustavo142f](https://github.com/Gustavo142f)
- 📧 Repositório: [github-repo](https://github.com/Gustavo142f/github-repo)

---

## ⭐ Se Gostou

Dê uma estrela neste repositório! ⭐

---

## 📚 Recursos Úteis

- [Python Docs](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Real Python](https://realpython.com/)
- [GeeksforGeeks Python](https://www.geeksforgeeks.org/python-programming-language/)

---

**Criado com ❤️ como Engenharia de Software Python**

*Última atualização: 12 de agosto de 2026*

---

## 📞 Suporte

Dúvidas? Verifique:
1. [GUIA_EXECUCAO.md](GUIA_EXECUCAO.md) para instruções
2. [INDICE.md](INDICE.md) para navegar
3. [MAPEAMENTO_NOTEBOOK.md](MAPEAMENTO_NOTEBOOK.md) para origem do código
4. Comente em uma Issue do GitHub

Bom aprendizado! 🎓
