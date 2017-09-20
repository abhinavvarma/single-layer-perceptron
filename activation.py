import math


def threshold(k, theta):
    ''' Threshold activation function'''
    return (0 if k < theta else 1)


def sigmoid(k):
    '''Sigmoid activation function '''
    return 1/(1+math.exp(-k))


def tanh(k):
    ''' Tanh activation function '''
    return math.tanh(k)


def relu(k):
    ''' ReLu activation function '''
    return max(0, k)


ALLOWED_TYPES = {
    "threshold": threshold,
    "tanh": tanh,
    "relu": relu
}