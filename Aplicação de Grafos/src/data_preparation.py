import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_and_normalize_data(file_path):
    # Carregar os dados
    data = pd.read_csv(file_path)

    # Remover colunas com apenas NaN
    data = data.dropna(axis=1, how='all')

    # Selecionar apenas as colunas numéricas
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    # Normalizar as colunas numéricas
    scaler = MinMaxScaler()
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

    return data
