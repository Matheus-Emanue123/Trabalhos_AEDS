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
  - `script.sh`: Script shell, que pode ser rodado com um `./run.sh`, que limpa os arquivos de entrada e saída, gera uma matriz aleatória e a insere no arquivo de entrada e então roda os comandos do makefile 
  para a linguagem C.
  ```

## Implementação
Nossa implementação consiste em... (descreva a implementação aqui, explicando cada função).

## Curiosidades
Existem várias configurações interessantes no Jogo da Vida, como os "osciladores". Um exemplo é o 4x4 de 1, que... (descreva a curiosidade aqui).

## Compilação
Existem duas maneiras de compilar e executar o programa:

1. **Compilar gerando a matriz aleatoriamente**: Após instalar Python e NumPy, você pode usar o script shell para gerar uma matriz aleatória. Basta executar `./run.sh` no terminal, fornecer a quantidade de gerações e a matriz será gerada aleatoriamente.

2. **Utilizar matriz própria**: Se você quiser usar sua própria matriz, pode inseri-la no arquivo `input.mps` e executar `make` e `make run` no terminal.


Neste exemplo, cada item indenta é um subdiretório ou arquivo do item acima dele. Você pode ajustar isso para refletir a estrutura real do seu projeto.

Se você quiser adicionar descrições para cada arquivo ou diretório, você pode fazer isso em uma lista. Aqui está um exemplo: