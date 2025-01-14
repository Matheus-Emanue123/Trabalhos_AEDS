# Análise de Sistemas Estelares com Grafos e Similaridade à Terra

## Descrição do Projeto

Este projeto utiliza **grafos**, **técnicas de machine learning** e algoritmos de **similaridade** para analisar sistemas estelares e identificar planetas semelhantes à Terra. O objetivo principal é construir uma estrutura interativa e escalável que permita explorar dados de exoplanetas, criar visualizações e detectar padrões ou clusters que indiquem planetas habitáveis ou com características similares às da Terra.

---

## Funcionalidades Principais

- **Carregamento e Normalização de Dados:**
  - Carrega arquivos CSV de dados estelares.
  - Normaliza colunas numéricas para facilitar comparações.

- **Identificação de Similaridade:**
  - Implementa um método baseado na **diferença relativa** entre os parâmetros dos planetas e os da Terra.
  - Filtra planetas com características semelhantes.

- **Construção de Grafos Interativos:**
  - Usa bibliotecas como `NetworkX` e `PyVis` para criar grafos interativos.
  - Representa planetas como nós e suas similaridades como arestas.

- **Hashing Local Sensível (LSH):**
  - Agrupa planetas semelhantes usando assinaturas binárias geradas por LSH.

- **Visualização e Clustering:**
  - Exibe grafos com clusters identificados de planetas semelhantes.
  - Detecta comunidades no grafo usando algoritmos de modularidade.

---

## Estrutura do Projeto

### Arquivos

1. **`data_preparation.py`**
   - Carrega e normaliza os dados para análise.
   - Remove valores ausentes e escalona colunas numéricas para o intervalo [0, 1].

2. **`comparison.py`**
   - Define funções para verificar a similaridade de planetas com a Terra.
   - Aplica filtros baseados em tolerâncias configuráveis.

3. **`graph_construction_interactive.py`**
   - Constrói grafos interativos com base nos dados.
   - Gera arquivos HTML para visualização no navegador.

4. **`main.py`**
   - Integra as funcionalidades principais:
     - Carregamento de dados.
     - Aplicação de LSH.
     - Criação de grafos para grupos de planetas semelhantes.

5. **`visualization.py`**
   - Oferece métodos para visualização estática e detecção de clusters em grafos.

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Bibliotecas**:
  - `pandas`: Manipulação de dados.
  - `scikit-learn`: Normalização e técnicas de machine learning.
  - `NetworkX`: Construção e análise de grafos.
  - `PyVis`: Visualização interativa de grafos.
  - `Matplotlib`: Visualização estática de grafos.

---

## Como Executar

### Pré-requisitos

- Python 3.8+ instalado.
- Dependências instaladas via `pip`:
  ```bash
  pip install pandas scikit-learn networkx pyvis matplotlib
