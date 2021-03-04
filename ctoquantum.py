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
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j].real**2 + mat[i][j].imag**2

    result = np.dot(mat, state)
    for i in range(t - 1):
        result = np.dot(mat, result)

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
