#include "jogoDaVida.h"

int main() {

    int tabuleiro** = (int**) malloc(10 * sizeof(int*));
    
    inicializar_tabuleiro(tabuleiro);
    for (int i = 0; i < 10; i++) {
        exibir_tabuleiro(tabuleiro);
        salvar_em_arquivo(tabuleiro, "geracoes.mps");
        proxima_geracao(tabuleiro);
    }
    return 0;
}