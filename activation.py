import math


def threshold(k, theta):
    if k < theta:
        return 0
    else:
        return 1


def logistic(k, theta):
    return 0.5 + 0.5 * math.tanh((k - theta)/2)


def relu(k, theta):
    return max(0, k - theta)


ALLOWED_TYPES = {
    "threshold": threshold,
    "tanh": logistic,
    "relu": relu
}