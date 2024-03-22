#include <random>
#include "GerarVetores.hpp"

std::vector<int> gerarVetorAleatorio(int tamanho) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, 1000);

    std::vector<int> vec(tamanho);
    for (int i = 0; i < tamanho; i++) {
        vec[i] = dis(gen);
    }
    return vec;
}