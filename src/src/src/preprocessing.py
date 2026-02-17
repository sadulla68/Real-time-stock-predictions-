import numpy as np
from sklearn.preprocessing import MinMaxScaler

def prepare_data(df):
    features = df[["Close"]]

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(features)

    X, y = [], []
    window = 60

    for i in range(window, len(scaled)):
        X.append(scaled[i-window:i])
        y.append(scaled[i, 0])

    return np.array(X), np.array(y), scaler
