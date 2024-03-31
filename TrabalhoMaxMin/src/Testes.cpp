#include "Testes.hpp"
#include "GerarVetores.hpp"
#include "MaxMin.hpp"
#include <iostream>
#include <algorithm>
#include <chrono>
#include <fstream>

void executarTestes() {
    std::vector<int> vetores[] = {gerarVetorAleatorio(1000), gerarVetorAleatorio(10000), gerarVetorAleatorio(100000), gerarVetorAleatorio(500000)};
    int max, min;
    std::ofstream file("resultados.mps");

    std::vector<std::function<void(std::vector<int>&, int&, int&)>> funcoes = {MaxMin1, MaxMin2, MaxMin3};
    std::vector<std::string> estados = {"aleatório", "crescente", "decrescente"};

    for(auto& funcao : funcoes) {
        for(int i = 0; i < sizeof(vetores)/sizeof(vetores[0]); i++) {
            auto vetor = vetores[i]; 
            for(auto& estado : estados) {
                if(estado == "crescente") std::sort(vetor.begin(), vetor.end());
                else if(estado == "decrescente") std::sort(vetor.rbegin(), vetor.rend());

                std::chrono::duration<double> tempo_total;
                for(int j = 0; j < 10; j++) {
                    auto inicio = std::chrono::high_resolution_clock::now();
                    funcao(vetor, max, min);
                    auto fim = std::chrono::high_resolution_clock::now();
                    tempo_total += std::chrono::duration_cast<std::chrono::microseconds>(fim - inicio);
                }
                tempo_total /= 10.0;
                std::string output = "Vetor " + std::to_string(i+1) + ", Max: " + std::to_string(max) + ", Min: " + std::to_string(min) + ", Tempo médio (" + estado + "): " + std::to_string(tempo_total.count()) + " microssegundos\n";
                std::cout << output;
                file << output;
                file.flush(); 
                            }
        }
    }
    file.close();
}