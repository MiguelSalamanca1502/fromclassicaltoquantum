import numpy as np
import matplotlib.pyplot as plt


def marbles(mat, state, t):
    result = np.dot(mat, state)
    for i in range(t - 1):
        result = np.dot(mat, result)
    return result


def multSlits(mat, state, t):
    result = np.dot(mat, state)
    for i in range(t - 1):
        result = np.dot(mat, result)
    return result

def quantumMultSlits(mat, state, t):
    result = np.dot(mat, state)
    for i in range(t - 1):
        result = np.dot(mat, result)

    for i in range(len(result)):
        result[i][0] = np.abs(result[i][0])**2
    return result

def plot(state):
    estados = [i for i in range(len(state))]
    fig, ax = plt.subplots()
    ax.set_ylabel('Probabilidades')
    ax.set_xlabel('Estados')
    ax.set_title('Sistema Cuantico')
    plt.bar(estados, state)
    plt.savefig('probabilities.png')
    plt.show()
