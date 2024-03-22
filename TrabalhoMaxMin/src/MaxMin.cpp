#include "MaxMin.hpp"

void MaxMin1(std::vector<int>& A, int& Max, int& Min) {
    Max = A[0], Min = A[0];
    for(int i = 1; i < A.size(); i++) {
        if(A[i] > Max) Max = A[i];
        if(A[i] < Min) Min = A[i];
    }
}

void MaxMin2(std::vector<int>& A, int& Max, int& Min) {
    Max = A[0], Min = A[0];
    for(int i = 1; i < A.size(); i++) {
        if(A[i] > Max) Max = A[i];
        else if(A[i] < Min) Min = A[i];
    }
}

void MaxMin3(std::vector<int>& A, int& Max, int& Min) {
    int FimDoAnel;
    if (A.size() % 2 > 0) {
        A.push_back(A.back());
        FimDoAnel = A.size() - 1;
    } else {
        FimDoAnel = A.size() - 2;
    }

    if (A[0] > A[1]) {
        Max = A[0];
        Min = A[1];
    } else {
        Max = A[1];
        Min = A[0];
    }

    int i = 2;
    while (i <= FimDoAnel) {
        if (A[i] > A[i+1]) {
            if (A[i] > Max) Max = A[i];
            if (A[i+1] < Min) Min = A[i+1];
        } else {
            if (A[i+1] > Max) Max = A[i+1];
            if (A[i] < Min) Min = A[i];
        }
        i += 2;
    }
}
