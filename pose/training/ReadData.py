import numpy as np

from sklearn.utils import shuffle
from math import ceil

def read_data_files(data_files, limit_data_count):
    # Asegúrese de que las rutas de archivo estén presentes en una lista
    # Se etiquetará según la entrada en la lista
    # limit_data_count: límite superior de la cantidad de entradas permitidas para cada tipo.
    X_data, y_data = None, None
    for label_index, data_file in enumerate(data_files):
        data = np.genfromtxt(data_file, delimiter = ',')
        data = data[:limit_data_count, :]
        print(data.dtype)
        labels = [label_index] * data.shape[0]
        if X_data is None:
            X_data = data
            y_data = labels
        else:
            X_data = np.append(X_data, data, axis = 0)
            y_data.extend(labels)

    return X_data, y_data

def split_data(X_data, y_data, split_ratio):
    X_data, y_data = shuffle(X_data, y_data)
    split_at = int(ceil(len(y_data) * split_ratio))
    X_train, y_train = X_data[:split_at, :], y_data[:split_at]
    X_test, y_test = X_data[split_at:, :], y_data[split_at:]
    return (X_train, y_train), (X_test, y_test)

