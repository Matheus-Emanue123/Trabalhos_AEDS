#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "jogoDaVida.h"



void inicializar_tabuleiro(int tabuleiro[N][N]) {
    srand(time(NULL));
    int N = rand() % 16 + 5; // Gera um número aleatório entre 5 e 20
    int x = (N * N) / 3;
    int count = 0;

    // Preenche a matriz com 0s e 1s
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (count < x) {
                tabuleiro[i][j] = 1;
                count++;
            } else {
                tabuleiro[i][j] = 0;
            }
        }
    }

    // Embaralha a matriz
    for (int i = N - 1; i > 0; i--) {
        for (int j = N - 1; j > 0; j--) {
            int i2 = rand() % (i + 1);
            int j2 = rand() % (j + 1);
            int temp = tabuleiro[i][j];
            tabuleiro[i][j] = tabuleiro[i2][j2];
            tabuleiro[i2][j2] = temp;
        }
    }

    // Salva a matriz no arquivo input.mps
    FILE *arquivo = fopen("datasets/input.mps", "w");
    if (arquivo == NULL) {
        printf("Não foi possível abrir o arquivo input.mps\n");
        exit(1);
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            fprintf(arquivo, "%d ", tabuleiro[i][j]);
        }
        fprintf(arquivo, "\n");
    }
    fclose(arquivo);
}

void exibir_tabuleiro(int tabuleiro[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", tabuleiro[i][j]);
        }
        printf("\n");
    }
}

void salvar_em_arquivo(int tabuleiro[N][N], char *nome_arquivo) {
    FILE *arquivo = fopen(nome_arquivo, "a");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            fprintf(arquivo, "%d ", tabuleiro[i][j]);
        }
        fprintf(arquivo, "\n");
    }
    fprintf(arquivo, "\n");
    fclose(arquivo);
}

void proxima_geracao(int tabuleiro[N][N]) {
    int novo_tabuleiro[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int vizinhos_vivos = 0;
            for (int di = -1; di <= 1; di++) {
                for (int dj = -1; dj <= 1; dj++) {
                    if (di == 0 && dj == 0) continue;
                    int ni = i + di;
                    int nj = j + dj;
                    if (ni >= 0 && ni < N && nj >= 0 && nj < N && tabuleiro[ni][nj] == 1) {
                        vizinhos_vivos++;
                    }
                }
            }
            novo_tabuleiro[i][j] = (tabuleiro[i][j] == 1 && vizinhos_vivos >= 2 && vizinhos_vivos <= 3) || (tabuleiro[i][j] == 0 && vizinhos_vivos == 3);
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            tabuleiro[i][j] = novo_tabuleiro[i][j];
        }
    }
}