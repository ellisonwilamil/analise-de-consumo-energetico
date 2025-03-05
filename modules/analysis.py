# Funções de análise (métricas, modelos, etc.)
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def random_forest(df):
    X = df[['ta', 'tb', 'tc', 'fpa', 'fpb', 'fpc', 'q3']].values
    y = df['p3'].values
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)
    pred = model.predict(X[:5])  # Teste inicial
    return pred

