#ifndef JOGODAVIDA_H
#define JOGODAVIDA_H

#define N 5

void inicializar_tabuleiro(int tabuleiro[N][N]);
void exibir_tabuleiro(int tabuleiro[N][N]);
void salvar_em_arquivo(int tabuleiro[N][N], char *nome_arquivo);
void proxima_geracao(int tabuleiro[N][N]);

#endif