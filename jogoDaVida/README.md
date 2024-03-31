<div align="center">
    <img src="./img/logo.jpeg" width="200" height="200">
</div>

<div align="center">

## Jogo da Vida

</div>

## Introdução
O Jogo da Vida é um autômato celular concebido pelo matemático britânico John Horton Conway em 1970. É um jogo de zero jogadores, o que significa que sua evolução é determinada por seu estado inicial, não necessitando de nenhuma entrada de dados posterior.

## Objetivos
O objetivo deste exercício é utilizar conhecimentos de programação para manipular uma matriz 2D de células, seguindo as regras do Jogo da Vida. As regras são as seguintes: 

- Uma célula viva com menos de dois vizinhos vivos morre (solidão).
- Uma célula viva com mais de três vizinhos vivos morre (superpopulação).
- Uma célula viva com dois ou três vizinhos vivos sobrevive.
- Uma célula morta com exatamente três vizinhos vivos se torna viva (reprodução).

## Organização dos Arquivos
Os arquivos criados para o funcionamento do projeto estão dispostos da seguinte maneira do diretório:

```markdown
- - `/jogoDaVida`: Diretório raiz do projeto.
  - `/build`: Diretório gerado ao usar o Makefile.
  - `/datasets`: Diretório para os arquivos de entrada e saída.
    - `input.mps`: Arquivo de entrada.
    - `geracoes.mps`: Arquivo de saída.
  - `/img`: Diretório para imagens. Contém o logo do projeto e prints do código.
  - `/src`: Diretório para o código fonte.
    - `gerador.py`: Script Python para gerar uma matriz aleatória, 
    caso o usuário deseje.
    - `main.c`: Arquivo principal do projeto em C.
    - `jogoDaVida.c`: Arquivo com a implementação do Jogo da Vida.
    - `jogoDaVida.h`: Arquivo de cabeçalho para `jogoDaVida.c`.
  - `README.md`: Este arquivo.
  - `Makefile`: Makefile para compilar o projeto.
  - `run.sh`: Script shell, que pode ser rodado com um `./run.sh`, 
  que limpa os arquivos de entrada e saída, gera uma matriz aleatória 
  e a insere no arquivo de entrada e então roda os comandos do makefile 
  para a linguagem C.
  ```

## Ambiente de Criação

O código foi desenvolvido utilizando as seguintes ferramentas:

[![Linguagem](https://img.shields.io/badge/Linguagem-C-blue)](https://www.w3schools.com/c/c_intro.php)
[![IDE](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-blueviolet)](https://code.visualstudio.com/docs/?dv=linux64_deb)
[![ISO](https://img.shields.io/badge/ISO-Ubuntu%20Linux%2022.04-red)](https://ubuntu.com/)

## Implementação

### Funções

#### `verificaVizinhos (int **matriz, int linha, int coluna, int N)`

Esta função verifica os vizinhos de uma célula específica na matriz. Ela retorna o número de vizinhos vivos ao redor da célula na posição (linha, coluna).

```c
int verificaVizinhos(int **matriz, int linha, int coluna, int N) {
    int direcaoLinha[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    int direcaoColuna[] = {-1, 0, 1, -1, 1, -1, 0, 1};
    int vizinhosVivos = 0;

    for (int i = 0; i < 8; i++) {
        int novaLinha = linha + direcaoLinha[i], novaColuna = coluna + direcaoColuna[i];
        if (novaLinha >= 0 && novaLinha < N && novaColuna >= 0 && novaColuna < N && matriz[novaLinha][novaColuna]) {
            vizinhosVivos++;
        }
    }

    return vizinhosVivos;
}
```

#### aplicaRegras (int **matriz, int N)
Esta função aplica as regras do Jogo da Vida para a matriz atual. Ela cria uma nova matriz, copia o estado atual da matriz original para a nova matriz e então aplica as regras do Jogo da Vida. Após aplicar as regras, ela atualiza a matriz original com o estado da nova matriz.

```c
void aplicaRegras(int **matriz, int N) {
    int **novaMatriz;

    novaMatriz = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        novaMatriz[i] = (int *)malloc(N * sizeof(int));
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            novaMatriz[i][j] = matriz[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int vizinhosVivos = verificaVizinhos(matriz, i, j, N);

            if (matriz[i][j] && (vizinhosVivos < 2 || vizinhosVivos > 3)) {
                novaMatriz[i][j] = 0;
            }
            else if (!matriz[i][j] && vizinhosVivos == 3) {
                novaMatriz[i][j] = 1;
            }
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            matriz[i][j] = novaMatriz[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        free(novaMatriz[i]);
    }
    free(novaMatriz);
}
```

#### imprimeMatriz (int **matriz, int N)
Esta função imprime a matriz atual no arquivo de saída.

```c
void imprimeMatriz(int **matriz, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}
```

## Exemplos de Uso

Aqui estão alguns exemplos de entradas e saídas esperadas:

### Exemplo 1

**Entrada:**

Suponha que temos a seguinte matriz como entrada:

```
0 1 0 0 1 1
1 1 1 0 1 1
0 1 1 0 0 1
1 1 1 1 0 1
1 0 1 1 1 0
0 1 1 0 0 1
```

**Saída:**

A saída para caso o jogador escolha 5 gerações a serem feitas é:

```

Geração Inicial:        Geração 1:        Geração 2:        Geração 3:        

0 1 0 0 1 1             1 1 1 1 1 1       1 1 1 1 1 0       1 0 0 0 1 0         
1 1 1 0 1 1             1 0 0 0 0 0       1 0 1 1 0 1       1 0 0 0 0 0   
0 1 1 0 0 1             0 0 0 0 0 1       0 0 0 0 0 0       0 0 0 1 0 1    
1 1 1 1 0 1             1 0 0 0 0 1       0 0 0 0 1 1       0 0 0 0 1 1   
1 0 1 1 1 0             1 0 0 0 0 1       1 0 0 0 1 1       0 0 0 0 1 1           
0 1 1 0 0 1             0 1 1 0 1 0       0 1 0 0 0 0       0 0 0 0 0 0         

```



## Curiosidades
Existem várias configurações interessantes no Jogo da Vida, como os "osciladores". Um exemplo é o 4x4 de 1, que... (descreva a curiosidade aqui).

## Compilação
Existem duas maneiras de compilar e executar o programa:

1. **Compilar gerando a matriz aleatoriamente**: Após instalar Python e NumPy, você pode usar o script shell para gerar uma matriz aleatória. Basta executar `./run.sh` no terminal, fornecer a quantidade de gerações e a matriz será gerada aleatoriamente.

2. **Utilizar matriz própria**: Se você quiser usar sua própria matriz, pode inseri-la no arquivo `input.mps` e executar `make` e `make run` no terminal.
