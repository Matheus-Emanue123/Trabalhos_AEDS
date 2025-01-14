import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cdist
from graph_construction_interactive import construct_graph_interactive


def main_with_log_transform():
    print("Executando a versão com transformações logarítmicas...")

    # Configurações
    data_file = r"C:\Users\hecla\OneDrive\Área de Trabalho\CEFET\3 periodo\AEDS II\TRABALHOS\trabalho 01 indiviudal\databases\normalized_cumulative.csv"
    comparison_columns = ["koi_prad", "koi_teq", "koi_period", "koi_insol", "koi_sma"]

    # Dados da Terra
    earth_reference = {
        "koi_prad": 1.0,
        "koi_teq": 288.0,
        "koi_period": 365.25,
        "koi_insol": 1.0,
        "koi_sma": 1.0
    }

    # Dados artificiais semelhantes à Terra
    similar_earth_reference = {
        "koi_prad": 1.01,
        "koi_teq": 290.0,
        "koi_period": 365.0,
        "koi_insol": 1.02,
        "koi_sma": 1.01
    }

    # Carregar e preparar os dados
    data = pd.read_csv(data_file)
    data = data.iloc[:100]  # Limitar a 100 linhas para agilizar a execução
    data = data[comparison_columns].fillna(data[comparison_columns].median())

    # Adicionar Terra e planeta artificial
    data = pd.concat([
        data,
        pd.DataFrame([earth_reference, similar_earth_reference], columns=comparison_columns)
    ], ignore_index=True)

    # Transformações logarítmicas (adicionando uma constante para evitar log(0))
    log_data = np.log(data + 1)

    # Normalização MinMaxScaler após log
    scaler = MinMaxScaler()
    normalized_data = pd.DataFrame(
        scaler.fit_transform(log_data),
        columns=comparison_columns
    )

    # Função para calcular distância de Mahalanobis
    def mahalanobis_distance(data):
        covariance_matrix = np.cov(data.T)
        inv_covariance_matrix = np.linalg.inv(covariance_matrix)
        mean = data.mean(axis=0)
        distances = cdist(data, [mean], metric='mahalanobis', VI=inv_covariance_matrix)
        return distances

    # Gerar os 3 grafos
    construct_graph_interactive(normalized_data, comparison_columns, tolerance=0.5, output_html="graph_euclidean_log.html")
    construct_graph_interactive(normalized_data, comparison_columns, tolerance=0.5, output_html="graph_manhattan_log.html")
    distances_mahalanobis = mahalanobis_distance(normalized_data.values)
    print("Distâncias Mahalanobis calculadas:", distances_mahalanobis)


if __name__ == "__main__":
    main_with_log_transform()
