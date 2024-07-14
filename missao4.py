import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

class DespesasTimeSeries:
    def __init__(self, datas, despesas):
        self.datas = pd.to_datetime(datas, format='%Y-%m')
        self.despesas = np.array(despesas)

class RegressaoLinear:
    def __init__(self, time_series):
        self.time_series = time_series
        self.model = LinearRegression()

    def ajustar_modelo(self):
        X = self.time_series.datas.map(pd.Timestamp.toordinal).values.reshape(-1, 1)
        y = np.array(self.time_series.despesas).reshape(-1, 1)
        self.model.fit(X, y)

    def get_predicoes(self):
        X = self.time_series.datas.map(pd.Timestamp.toordinal).values.reshape(-1, 1)
        return self.model.predict(X)

class Graficos:
    def __init__(self, time_series_list, regressao_list):
        self.time_series_list = time_series_list
        self.regressao_list = regressao_list

    def plotar_grafico_linha(self):
        plt.figure(figsize=(10, 6))
        for time_series in self.time_series_list:
            plt.plot(time_series.datas, time_series.despesas, marker='o', label=time_series.nome)
        plt.xlabel('Data')
        plt.ylabel('Valor')
        plt.title('Despesas')
        plt.grid(True)
        plt.legend()
        plt.show()

    def plotar_regressao_linear(self):
        plt.figure(figsize=(10, 6))
        for time_series, regressao in self.regressao_list:
            plt.scatter(time_series.datas, time_series.despesas, label='Despesas')
            plt.plot(time_series.datas, regressao.get_predicoes(), label='Regressão Linear')
        plt.xlabel('Data')
        plt.ylabel('Valor')
        plt.title('Regressão Linear das Despesas')
        plt.legend()
        plt.grid(True)
        plt.show()

def processar_e_plotar(dados):
    time_series_list = []
    regressao_list = []
    for categoria, data in dados.items():
        time_series = DespesasTimeSeries(data['datas'], data['despesas'])
        time_series.nome = categoria
        regressao = RegressaoLinear(time_series)
        regressao.ajustar_modelo()
        time_series_list.append(time_series)
        regressao_list.append((time_series, regressao))

    graficos = Graficos(time_series_list, regressao_list)
    graficos.plotar_grafico_linha()
    graficos.plotar_regressao_linear()

dados = {
    "Transporte": {
        "datas": ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05',
                  '2024-06', '2024-07', '2024-08', '2024-09', '2024-10'],
        "despesas": [100, 200, 180, 250, 190, 110, 160, 180, 200, 220]
    },
    "Alimentação": {
        "datas": ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05',
                  '2024-06', '2024-07', '2024-08', '2024-09', '2024-10'],
        "despesas": [400, 500, 650, 575, 553, 440, 760, 510, 413, 444]
    },
    "Roupas": {
        "datas": ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05',
                  '2024-06', '2024-07', '2024-08', '2024-09', '2024-10'],
        "despesas": [200, 120, 99.99, 130.33, 125, 60.99, 39.90, 360, 300, 800]
    }
}

processar_e_plotar(dados)
