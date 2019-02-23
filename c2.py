import random
import numpy as np

def generate_data(sample_size:int)->tuple:
    mean_blue = [1, 0]
    mean_orange = [0, 1]
    mean_cov = np.eye(2)
    mean_size = 10

    sample_cov = np.eye(2)/5

    sample_blue_mean = np.random.multivariate_normal(mean_blue, mean_cov, mean_size)
    sample_orange_mean = np.random.multivariate_normal(mean_orange, mean_cov, mean_size)

    sample_blue = np.array([
        np.random.multivariate_normal(sample_blue_mean[random.randint(0, 9)], sample_cov)
        for _ in range(sample_size)
    ])
    y_blue = [0 for _ in range(sample_size)]

    sample_orange = np.array([
        np.random.multivariate_normal(sample_orange_mean[random.randint(0, 9)], sample_cov)
        for _ in range(sample_size)
    ])
    y_orange = [1 for _ in range(sample_size)]

    data_x = np.concatenate((sample_blue, sample_orange), axis=0)
    data_y = np.concatenate((y_blue, y_orange))

    return data_x, data_y
