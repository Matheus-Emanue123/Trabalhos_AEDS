#include "Testes.hpp"
#include "GerarVetores.hpp"
#include "MinMax.hpp"
#include <iostream>
#include <algorithm>
#include <chrono>
#include <fstream>

void executarTestes() {
    std::vector<int> vetores[] = {gerarVetorAleatorio(1000), gerarVetorAleatorio(10000), gerarVetorAleatorio(100000), gerarVetorAleatorio(500000)};
    int max, min;
    std::ofstream file("resultados.mps");

    std::vector<std::function<void(std::vector<int>&, int&, int&)>> funcoes = {MinMax1, MinMax2, MinMax3};
    std::vector<std::string> estados = {"aleatório", "crescente", "decrescente"};

    std::vector<std::string> nomesFuncoes = {"MinMax1", "MinMax2", "MinMax3"};
    
    // ...
std::ofstream fileCSV("resultados.csv");
    fileCSV << "Função,Tamanho,Decrescente,Desordenado,Crescente\n";

    for (int f = 0; f < funcoes.size(); f++) {
        auto& funcao = funcoes[f];
        for (int i = 0; i < sizeof(vetores) / sizeof(vetores[0]); i++) {
            std::vector<double> tempos(3, 0.0);
            for (int e = 0; e < estados.size(); e++) {
                auto vetor = vetores[i];
                if (estados[e] == "crescente") std::sort(vetor.begin(), vetor.end());
                else if (estados[e] == "decrescente") std::sort(vetor.rbegin(), vetor.rend());

                std::chrono::duration<double> tempo_total;
                for (int j = 0; j < 10; j++) {
                    auto inicio = std::chrono::high_resolution_clock::now();
                    funcao(vetor, max, min);
                    auto fim = std::chrono::high_resolution_clock::now();
                    auto tempo_execucao = std::chrono::duration_cast<std::chrono::microseconds>(fim - inicio);
                    tempo_total += tempo_execucao;
                }
                tempo_total /= 10.0;
                tempos[e] = std::chrono::duration<double, std::micro>(tempo_total).count();
            }
            fileCSV << f + 1 << "," << (i == 0 ? 1000 : (i == 1 ? 10000 : (i == 2 ? 100000 : 500000))) << "," 
                    << tempos[2] << "," << (i == 0 ? 1000 : (i == 1 ? 10000 : (i == 2 ? 100000 : 500000))) << "," 
                    << tempos[0] << "," << (i == 0 ? 1000 : (i == 1 ? 10000 : (i == 2 ? 100000 : 500000))) << "," 
                    << tempos[1] << "\n";
            fileCSV.flush();
        }
    }
    fileCSV.close();
}