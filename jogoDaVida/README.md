<div align="center">
    <img src="./img/logo.jpeg" width="200" height="200">
</div>

<div align="center">

##  🖤 Jogo da Vida

</div>

<h2 align="center"> Sumário </h2>
    <h4 align="center"> 
        
 [Introdução](#introdução)

 [Objetivos](#objetivos)

 [Ambiente de Criação](#ambiente-de-criação)
  
 [Organização dos Arquivos](#organização-dos-arquivos)

 [Implementação](#implementação)

 [Arquivos adicionais](#arquivos-adicionais)

 [Casos de Teste](#casos-de-teste)

 [Curiosidades - Osciladores](#curiosidades---osciladores)

 [Ambiente de Testes](#ambiente-de-testes)

 [Compilação e Execução](#compilação-e-execução)

 [Conclusão](#Conclusão)

 [Créditos](#Créditos)

 [Contato](#contato)

## ☕ Introdução
O Jogo da Vida é um autômato celular concebido pelo matemático britânico John Horton Conway e m 1970. É um jogo de zero jogadores, o que significa que sua evolução é determinada por seu estado inicial, não necessitando de nenhuma entrada de dados posterior.

## 🎯 Objetivos
O objetivo deste exercício é utilizar conhecimentos de programação para manipular uma matriz 2D de células, seguindo as regras do Jogo da Vida. As regras são as seguintes: 

- Uma célula viva com menos de dois vizinhos vivos morre (solidão).
- Uma célula viva com mais de três vizinhos vivos morre (superpopulação).
- Uma célula viva com dois ou três vizinhos vivos sobrevive.
- Uma célula morta com exatamente três vizinhos vivos se torna viva (reprodução).

## 🖥️ Ambiente de Criação

O código foi desenvolvido utilizando as seguintes ferramentas:

[![Linguagem](https://img.shields.io/badge/Linguagem-C-blue)](https://www.w3schools.com/c/c_intro.php)
[![IDE](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-blueviolet)](https://code.visualstudio.com/docs/?dv=linux64_deb)
[![ISO](https://img.shields.io/badge/ISO-Ubuntu%20Linux%2022.04-red)](https://ubuntu.com/)

## 📂 Organização dos Arquivos
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
  - `run.1sh`: Script shell, que pode ser rodado com um `./run.sh`, 
  que limpa os arquivos de entrada e saída, gera uma matriz aleatória 
  e a insere no arquivo de entrada e então roda os comandos do makefile 
  para a linguagem C.
  - `run2.sh`: Script shell que realiza a mesma coisa que o `run1.sh`, 
  mas quando o usuário deseja compilar de maneira diferente. 
  ```
  [Verificar o tipo de compilação desejada](#compilação)

## 💡 Implementação

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

#### `aplicaRegras (int **matriz, int N)`
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

#### `imprimeMatriz (int **matriz, int N)`
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

### 📜 Arquivos adicionais

#### `Gerador de matriz em python`

Para facilitar os testes do projeto, foi criado um pequeno script em python, utilizando a biblioteca numpy, para gerar as matrizes do Jogo da Vida e inseri-las no arquivo de entrada `input.mps`.

```
import numpy as np

N = np.random.randint(2, 1000)

matriz = np.random.randint(0, 2, size=(N, N))

np.savetxt('../datasets/input.mps', matriz, fmt='%d')
```
#### `Scripts shell para automação`

Foram feitos dois scripts shell para facilitar a compilação do código, ambos sendo usados em casos diferentes de acordo com a vontade do usuário.

**script 1:**

```
#!/bin/bash

echo > ./datasets/geracoes.mps
echo > ./datasets/input.mps
cd ./src

python3 gerador.py

cd ..

make clean
make
make run
```

**script 2:**

```
#!/bin/bash

make clean
make
make run
```


## 🧪 Casos de Teste

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

Geração Inicial:        Geração 1:        Geração 2:        Geração 3:        Geração 4:        Geração 5:        

0 1 0 0 1 1             1 1 1 1 1 1       1 1 1 1 1 0       1 0 0 0 1 0       0 0 0 0 0 0       0 0 0 0 0 0           
1 1 1 0 1 1             1 0 0 0 0 0       1 0 1 1 0 1       1 0 0 0 0 0       0 0 0 0 1 0       0 0 0 0 0 0    
0 1 1 0 0 1             0 0 0 0 0 1       0 0 0 0 0 0       0 0 0 1 0 1       0 0 0 0 0 1       0 0 0 0 1 0    
1 1 1 1 0 1             1 0 0 0 0 1       0 0 0 0 1 1       0 0 0 0 1 1       0 0 0 1 0 0       0 0 0 0 0 1    
1 0 1 1 1 0             1 0 0 0 0 1       1 0 0 0 1 1       0 0 0 0 1 1       0 0 0 0 1 1       0 0 0 0 1 0            
0 1 1 0 0 1             0 1 1 0 1 0       0 1 0 0 0 0       0 0 0 0 0 0       0 0 0 0 0 0       0 0 0 0 0 0           

```

### Exemplo 2

No exercício proposto, a matriz de entrada deve ser no mínimo de ordem 5 (5 linhas x 5 colunas), então, quando uma matriz de ordem menor é inserida como entrada, o programa recusa a matriz e informa que ela é inválida, como no exemplo a seguir:

**Entrada:**

Uma matriz 4x4, inferior ao mínimo requerido:

```
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
```

**Saída:**

A saída para casos como esse, em que a matriz não atinge o tamanho mínimo esperado é:

```
A matriz não é válida, pois sua ordem é inferior a 5
```

## 🤔 Curiosidades - Osciladores
Durante os testes do projeto, foi percebido que no Jogo da Vida de Conway, existem certos padrões, que retornam ao seu estado inicial depois de finitas gerações. Após algumas pesquisas, foi descoberto que esse padrão é chamado de oscilador. Embora não faça parte do objetivo do trabalho proposto estudar esses osciladores, achei interessante abordar sobre eles. Seus tipos mais conhecidos são:

**1 - Blinker**

O Blinker é o oscilador mais simples no Jogo da Vida de Conway. Ele consiste em três células vivas dispostas em uma linha reta. Após cada geração ou período P, o Blinker "pisca" entre uma orientação vertical e uma orientação horizontal.

```
P. 01:          P. 02:          P. 03:

0 1 0           0 0 0           0 1 0
0 1 0           1 1 1           0 1 0
0 1 0           0 0 0           0 1 0 
```

Como demonstrado no exemplo acima, o Blinker retorna ao seu estado original após 2 gerações, por isso dizemos que ele tem um "período" de 2. No Jogo da Vida, o Blinker é um exemplo de um padrão que é estável, mas não estático: ele muda de forma, mas não se move e retorna ao seu estado original após um número finito de gerações.

**2 - Toad**

O Toad é um oscilador no Jogo da Vida de Conway que tem um período de 2. Ele consiste em duas linhas deslocadas de três células.

```
P. 01:          P. 02:          P. 03:

0 0 0 0         0 0 1 0         0 0 0 0 
0 1 1 1         1 0 0 1         0 1 1 1
1 1 1 0         1 0 0 1         1 1 1 0
0 0 0 0         0 1 0 0         0 0 0 0 
```

O Toad alterna entre esses dois estados a cada geração. Assim como o Blinker, o Toad é um exemplo de um padrão que é estável, mas não estático: ele muda de forma, mas não se move e retorna ao seu estado original após um número finito de gerações. Neste caso, o Toad retorna ao seu estado original a cada 2 gerações, por isso dizemos que ele tem um "período" de 2.

**3 - Beacon**

O Beacon, no Jogo da Vida de Conway, é um oscilador estável com um período de 2, alternando entre duas configurações a cada geração. Apesar de sua forma mudar, ele permanece na mesma localização e retorna à sua configuração inicial após duas gerações, caracterizando um padrão estável que oscila entre um conjunto limitado de estados.

```
P. 01:          P. 02:          P. 03:

1 1 0 0         1 1 0 0         1 1 0 0
1 1 0 0         1 0 0 0         1 1 0 0
0 0 1 1         0 0 0 1         0 0 1 1
0 0 1 1         0 0 1 1         0 0 1 1
```

**4 - Pulsar**

O Pulsar é um oscilador no Jogo da Vida de Conway que tem um período de 3. Ele é notável por ser o menor oscilador que é isolado, ou seja, não tem células vivas em sua vizinhança imediata.

```

P. 01:                         P. 02:                         P. 03:
0 0 1 1 1 0 0 0 1 1 1 0 0      0 0 0 0 0 0 0 0 0 0 0 0 0      0 0 1 1 1 1 1 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0      0 0 0 1 0 0 0 1 0 0 0 1 0 0    1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1 0 0 0 0 1      0 0 1 0 0 0 1 0 0 0 1 0 0 1    1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1 0 0 0 0 1      0 0 1 0 0 0 1 0 0 0 1 0 0 1    1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1 0 0 0 0 1      0 0 0 1 0 0 0 1 0 0 0 1 0 0    0 0 1 1 1 1 1 0 0 1 1 1 1 1 0 0
0 0 1 1 1 0 0 0 1 1 1 0 0      0 0 0 0 0 0 0 0 0 0 0 0 0 0    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0      0 0 0 1 0 0 0 1 0 0 0 1 0 0    0 0 1 1 1 1 1 0 0 1 1 1 1 1 0 0
0 0 1 1 1 0 0 0 1 1 1 0 0      0 0 1 0 0 0 1 0 0 0 1 0 0 1    1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1 0 0 0 0 1      0 0 1 0 0 0 1 0 0 0 1 0 0 1    1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1 0 0 0 0 1      0 0 0 1 0 0 0 1 0 0 0 1 0 0    1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0
1 0 0 0 0 1 0 1 0 0 0 0 1      0 0 0 0 0 0 0 0 0 0 0 0 0 0    0 0 1 1 1 1 1 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0      0 0 0 1 0 0 0 1 0 0 0 1 0 0    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 0 0 0 1 1 1 0 0      0 0 1 0 0 0 1 0 0 0 1 0 0 1    0 0 1 1 1 1 1 0 0 1 1 1 1 1 0 0
```

## 👨🏻‍🔬 Ambiente de Teste

Este projeto foi testado no seguinte ambiente:

- **Sistema Operacional**: Ubuntu 22.04
- **Compilador**: GCC 11.4.0
- **Hardware**: 11th Gen Intel(R) Core(TM) i5-11400H @ 2.70GHz, 8GB RAM, 512GB SSD

## 👨🏻‍💻 Compilação e Execução

Existem duas maneiras de compilar e executar o programa:

### 1. Compilar gerando a matriz aleatoriamente.
 Para compilar o projeto gerando uma matriz de entrada aleatória, será necessário seguir os seguintes passos:

#### 1.1 - Verificar a versão do python  instalada em seu computador.

O projeto foi feito com o python para linux na versão 3.10.12. Para checar a versão do python instalada, abra o terminal e execute o seguinte comando:

```
python --version
```

É muito comum no linux esse comando não ser reconhecido, caso seja este o seu caso tente executar o seguinte comando:

```
python3 --version
```

Se ainda assim você não obtiver êxito, pode ser que você não tenha o python instalado em sua máquina. Para instalá-lo, siga os passos a seguir:

1 - Primeiro, atualize sua lista de pacotes:

```
sudo apt update
```

2 - Em seguida, instale o Python:

```
sudo apt install python3
```

3 - Depois, instale o pip, que é o gerenciador de pacotes do Python:

```
sudo apt install python3-pip
```

4 - Verificar a versão do python instalada, com um dos comandos dados no item 1.

#### 1.2 - Instalar a biblioteca numpy do python.

O código em python do projeto utiliza a biblioteca numpy para gerar um número entre 2 e 1000, que será a ordem da matriz, e preenche ela aleatoriamente com 0's e 1's. Para instalar essa biblioteca, execute o seguinte comando

```
pip3 install numpy
```

#### 1.3 - Instalar o pacote make.
Como a compilação do projeto é feita por meio de um makefile, é necessário que o usuário tenha o pacote make instalado em seu computador. Isso pode ser feito executando a seguinte linha de comando:

```
sudo apt install make
```

Após isso, verifique a versão do make instalada. A versão instalada na máquina onde foram feitos os testes é a 4.3. Você pode checar a versão com o seguinte comando:

```
make --version
```

Se a versão do make instalada for muito superior ou inferior em comparação com a utilizada na craiação deste projeto, você pode desinstalá-la e verificar quais versões voce tem disponível.

Para isso, siga os passos:

1 - Desinstale o make do seu computador:

```
sudo apt remove make
```

2 - Verifique as versões disponíveis do pacote:

```
apt-cache policy make
```

3 - Instale a mesma versão utilizada pelo criador do projeto (4.3) ou a mais próxima possível:

```
sudo apt install make=<versão>
```
#### 1.4 - Dar permissão ao script shell e executar o comando.

Após isso, será necessário conceder permissão para o script shell em seu diretório - nesse caso, ao arquivo `run1.sh`. Para isso, digite esse comando no terminal:

```
chmod +x run1.sh
```

Caso você não tenha as permissões de escrita do script, será necessário utilizar sudo na frente do comando:

```
sudo chmod +x run1.sh
```

Após isso, basta executar o seguinte comando em seu terminal:

```
./run1.sh
```
Isso irá apagar todo o conteúdo dos arquivos de entrada `input.mps` e de saída `geracoes.mps`, irá compilar o `gerador.py` e inserir seu resultado dentro do arquivo de entrada. Após isso, irá limpar a pasta build, que contém o resultado da compilação anterior, caso exista, e realiza uma nova compilação, inserindo o resultado desta na pasta build. Caso a matriz seja válida, ou seja, de ordem 5 ou maior, o usuário fornece no console a quantidade N de gerações que deseja, e o resultado é impresso no arquivo geracoes.mps.

### 2. Utilizar matriz própria.
Se você deseje utilizar uma matriz específica no Jogo da Vida, você pode inseri-la manualmente no arquivo `input.mps` e seguir o [passo 1.3](#13---instalar-o-pacote-make) do tópico anterior e, posteriormente, retornar aqui. **Lembrando que a matriz deve, de preferência, ser quadrada**

#### 2.1 - Dar permissão ao script shell e executar o comando.

Depois te ter seguido os passos da instalação do pacote make, será necessário dar permissão para o script shell. Para isso, execute no terminal o comando a seguir:

```
chmod +x run2.sh
```

Novamente, caso você não tenha as permissões de escrita do script, será necessário utilizar sudo na frente do comando:

```
sudo chmod +x run2.sh
```

Isso irá apagar todo o conteúdo dos arquivos de entrada `input.mps` e de saída `geracoes.mps`. Após isso, irá limpar a pasta build, que contém o resultado da compilação anterior, caso exista, e realiza uma nova compilação, inserindo o resultado desta na pasta build, e então ler a primeira linha da matriz para verificar se ela é de ordem maior ou igual a 5, caso seja válida, o usuário fornece no console a quantidade N de gerações que deseja, e o resultado é impresso no arquivo geracoes.mps.

## 🔚 Conclusão 

Neste projeto, foi implementado o Jogo da Vida, um autômato celular concebido pelo matemático britânico John Horton Conway. Foi utilizada a linguagem de programação C para a implementação principal e Python para gerar matrizes aleatórias.

O projeto demonstrou a aplicação de conceitos de programação, como loops, condicionais e manipulação de arquivos. Além disso, foram utilizadas ferramentas de desenvolvimento de software, como Makefile e scripts shell, para automatizar o processo de compilação e execução do programa.

Espera-se que este projeto sirva como um recurso útil para quem está aprendendo programação e para quem está interessado em autômatos celulares e em simulações de sistemas complexos.

Agradeço por seu interesse em no projeto e convido você a contribuir com melhorias e extensões.

## 💭 Créditos

Este projeto usa um Makefile fornecido pelo professor [Michel Pires Silva](https://github.com/mpiress). Agradeço a ele por fornecer essa ferramenta útil para a compilação do projeto.

## 📪 Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo. Aqui estão algumas maneiras de fazer isso:

- Email: [memanuel643@gmail.com](mailto:memanuel643@gmail.com)
- LinkedIn: [Matheus Silva](www.linkedin.com/in/matheus-silva-emanuel)
- Instagram: [@mat_emanuel9](https://www.instagram.com/mat_emanuel9/)
- GitHub: [Matheus Emanuel](https://github.com/Matheus-Emanue123)

Estou ansioso para ouvir de você!
