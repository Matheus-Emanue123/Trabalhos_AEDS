import csv
import os

# Create directories for the output files
os.makedirs('PorFuncaoEstado', exist_ok=True)
os.makedirs('PorFuncaoVetor', exist_ok=True)

# Open the input file
with open('resultados.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    header = next(reader)  # Skip the header

    # Initialize the writers dictionary
    writers_funcao = {}

    # Process the rows
    for row in reader:
        funcao = row[0]
        vetor = row[1]
        estado = row[4]

        # Create file for each function
        file_name_funcao = f'PorFuncaoEstado/Resultados_{funcao}.csv'
        if file_name_funcao not in writers_funcao:
            writers_funcao[file_name_funcao] = csv.writer(open(file_name_funcao, 'w', newline=''))
            writers_funcao[file_name_funcao].writerow(header)  # Write the header

        writers_funcao[file_name_funcao].writerow(row)

        # Create file for each combination of Função and Vetor
        file_name_funcao_vetor = f'PorFuncaoVetor/Resultados_{funcao}_Vetor{vetor}.csv'
        if file_name_funcao_vetor not in writers_funcao:
            writers_funcao[file_name_funcao_vetor] = csv.writer(open(file_name_funcao_vetor, 'w', newline=''))
            writers_funcao[file_name_funcao_vetor].writerow(header)  # Write the header

        writers_funcao[file_name_funcao_vetor].writerow(row)
