import math


def threshold(k, *args):
    ''' Threshold activation function'''
    theta = args[0]
    return (0 if k < theta else 1)


def tanh(k, *args):
    ''' Tanh activation function '''
    return math.tanh(k)


def relu(k, *args):
    ''' ReLu activation function '''
    return max(0, k)


ALLOWED_TYPES = {
    "threshold": threshold,
    "tanh": tanh,
    "relu": relu
}