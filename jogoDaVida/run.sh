#!/bin/bash

echo > ./datasets/geracoes.mps
echo > ./datasets/input.mps
cd ./src

python3 gerador.py

cd ..

make clean
make
make run