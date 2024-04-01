#!/bin/bash

echo > ./datasets/geracoes.mps

make clean
make
make run