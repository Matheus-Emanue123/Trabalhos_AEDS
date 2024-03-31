#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "jogoDaVida.h"

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

void imprimeMatriz(int **matriz, int N) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", matriz[i][j]);
        }
        printf("\n");
    }
}

void executarJogoDaVida() {
    int N = 0;
    int **matriz;
    int numGeracoes;

    FILE *arquivo = fopen("datasets/input.mps", "r");
    if (arquivo == NULL) {
        printf("Não foi possível abrir o arquivo.\n");
        return;
    }

    char linha[1024];
    fgets(linha, sizeof(linha), arquivo);

    char *token = strtok(linha, " ");
    while (token != NULL) {
        N++;
        token = strtok(NULL, " ");
    }

    if (N < 5) {
        printf("A matriz não é válida, pois sua ordem é inferior a 5.\n");
        return;
    }

    else{
        printf("Digite o número de gerações: ");
    scanf("%d", &numGeracoes);}

    matriz = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        matriz[i] = (int *)malloc(N * sizeof(int));
    }

    rewind(arquivo);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!fscanf(arquivo, "%d", &matriz[i][j])) {
                break;
            }
        }
    }

    fclose(arquivo);

    FILE *saida = fopen("datasets/geracoes.mps", "w");
    if (saida == NULL) {
        printf("Não foi possível abrir o arquivo de saída.\n");
        return;
    }

    fprintf(saida, "Geração Inicial:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            fprintf(saida, "%d ", matriz[i][j]);
        }
        fprintf(saida, "\n");
    }

    for (int g = 0; g < numGeracoes; g++) {
        aplicaRegras(matriz, N);
        fprintf(saida, "Geração %d:\n", g + 1);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                fprintf(saida, "%d ", matriz[i][j]);
            }
            fprintf(saida, "\n");
        }
    }

    fclose(saida);

    for (int i = 0; i < N; i++) {
        free(matriz[i]);
    }
    free(matriz);
}